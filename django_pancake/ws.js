var ws = new WebSocket(
  'ws://' + window.location.host + '/ws'
)

ws.onopen = e => {
  // console.log('connected')
}

ws.onmessage = function (msg) {
  // console.log(msg.data)
  window.location.reload()
}

ws.onclose = function (e) {
  console.error('Connection to Live Server got closed.')
  console.warn('Please restart Live Server and reload this page.')
}
