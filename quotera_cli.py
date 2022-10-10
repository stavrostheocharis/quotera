#!./.venv/bin/python

import os
import typer
from typing import Optional
from enum import Enum
from termcolor import cprint
from pyfiglet import figlet_format

app = typer.Typer()


class Environment(str, Enum):
    dev = "dev"
    test = "test"
    staging = "staging"
    production = "production"


@app.command()
def serve(env: Optional[Environment] = Environment.dev, host: str = "0.0.0.0"):
    typer.echo(f"\nRunning Quotera API | Environment: {env} 🚀 \n")
    # check also dotmatrix
    typer.echo(cprint(figlet_format("Quotera", font="doom"), "green", attrs=["bold"]))
    os.system(
        f"ENV_FILE='.env.{env}' GUNICORN_CMD_ARGS='--keep-alive 0' uvicorn src.main:quotera --reload --host {host}"
    )


@app.command()
def serve_gunicorn(
    env: Optional[Environment] = Environment.dev,
    workers: int = 4,
    host: str = "0.0.0.0",
):
    typer.echo(f"\nRunning Quotera API with gunicorn | Environment: {env} 🚀 \n")
    os.system(
        f"ENV_FILE='.env.{env}' gunicorn -w {workers} -k uvicorn.workers.UvicornWorker --bind {host} src.main:quotera"
    )


@app.command("venv")
def create_venv():
    typer.echo("\nCreating virtual environment 🍇")
    os.system("python -m venv .venv")
    command = typer.style(
        "`source ./.venv/bin/activate`", fg=typer.colors.GREEN, bold=True
    )
    typer.echo(f"\nActivate with: {command}. Happy coding 😁 \n")


@app.command()
def install():
    # typer.echo("\nInstalling packages 🚀")
    os.system("pip install -r requirements.txt ")
    typer.echo(f"\nPackages installed. Have fun 😁 \n")
    typer.echo(f"\nInstalling nltk parts. 😁 \n")


@app.command()
def test(watch: bool = False):
    typer.echo("\nTesting package 🚀")
    if watch:
        os.system("ENV_FILE='.env.test' ptw")
        return
    os.system("ENV_FILE='.env.test' pytest")


@app.command()
def test_runner():
    typer.echo("\nTesting gitlab-runner 🚀")
    os.system("gitlab-runner exec docker api")


@app.command()
def docker_build(push: bool = False):
    typer.echo("\nBuilding docker image 🚀")
    os.system("docker build -t registry.gitlab.com/wysely/api:latest .")
    if push:
        typer.echo("\nPushing docker image 🚀")
        os.system("docker push registry.gitlab.com/wysely/api:latest")


@app.command("activate")
def activate_venv():
    typer.echo("\nActivate enviroment 🚀")
    os.system("source ./.venv/bin/activate")


@app.command("deactivate")
def deactivate_venv():
    typer.echo("\nDeactivate enviroment 🚀")
    os.system("deactivate")


if __name__ == "__main__":
    app()
