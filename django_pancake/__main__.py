import os
import typer

from django_pancake.command import make_many_pancakes, create_one_pancake
from django_pancake.server import start_server

app = typer.Typer()


@app.command()
def convert(
    target: str,
    output: str = None,
    inline: bool = False,
    replace: bool = False
) -> None:
    if os.path.isdir(target):
        make_many_pancakes(target, output)
    else:
        create_one_pancake(target, output, inline, replace)


@app.command()
def live(
    target: str
) -> None:
    start_server(target)


if __name__ == '__main__':
    app()
