import typer

if __name__ == '__main__':
    from django_pancake.command import command_app
    typer.run(command_app)