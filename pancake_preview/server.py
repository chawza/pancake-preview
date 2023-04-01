from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from django_pancake.make_pancakes import make_one_pancake
from watchfiles import awatch
import uvicorn

# source https://github.com/ajitid/live-server/blob/master/live_server/inject.py
script = """
var ws = new WebSocket( // eslint-disable-line
  'ws://' + window.location.host +
  '/ws')

ws.onopen = e => {
  console.log('connected')
}

ws.onmessage = function (msg) {
  // console.log(msg.data)
  window.location.reload()
}

ws.onclose = function (e) {
  console.error('Connection to Live Server got closed.')
  console.warn('Please restart Live Server and reload this page.')
}
"""


def inject_reload_script(html: str) -> str:
    global script

    # janky but good enough lol
    head_idx = html.find('</head>')
    if head_idx < 0:
        print('Cannot find <head> tag')
        return html

    tag = f'<script>{script}</script>'
    injected_html = html[:head_idx] + tag + html[head_idx:]

    return injected_html


def start_server(
    filepath: str,
    host='localhost',
    port=8001
):
    app = FastAPI()

    @app.get('/')
    async def view_template():
        pancake = make_one_pancake(template_path=filepath)
        pancake = inject_reload_script(pancake)
        return HTMLResponse(pancake)

    @app.websocket('/ws')
    async def wait_for_changes(ws: WebSocket):
        await ws.accept()
        async for changes in awatch(filepath):
            payload = {
                'instruction': 'reload',
                'changes': str(changes)
            }
            await ws.send_json(payload)

    uvicorn.run(app, host=host, port=port)
