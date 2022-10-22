import typer
from rich.console import Console
from src.streamlit_quotera.app import deploy_streamlit

app = typer.Typer()
console = Console()

@app.command()
def dashboard() -> None:
    """Deploys the streamlit dashboard."""
    deploy_streamlit()

if __name__ == "__main__":
    app()