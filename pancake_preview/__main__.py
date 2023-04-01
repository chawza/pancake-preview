import os
import typer

from pancake_preview.command import create_many_pancakes, create_one_pancake
from pancake_preview.server import start_server

app = typer.Typer()


@app.command()
def convert(
    target: str,
    output: str = None,
    inline: bool = False,
    replace: bool = False
) -> None:
    if os.path.isdir(target):
        create_many_pancakes(target, output, replace, inline)
    else:
        create_one_pancake(target, output, inline, replace)


@app.command()
def live(
    target: str
) -> None:
    if os.path.isdir(target):
        raise Exception('Cannot preveiew directory! specify filepath instead')
    start_server(target)


if __name__ == '__main__':
    app()
