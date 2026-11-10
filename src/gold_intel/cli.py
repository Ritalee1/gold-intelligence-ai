"""Command-line interface: ``gold-intel``."""

from typing import Annotated

import typer

from gold_intel import __version__
from gold_intel.config import get_settings

app = typer.Typer(
    name="gold-intel",
    help="Gold Intelligence AI: market intelligence and trading analytics.",
    no_args_is_help=True,
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"gold-intel {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-V",
            callback=_version_callback,
            is_eager=True,
            help="Show the version and exit.",
        ),
    ] = False,
) -> None:
    """Gold Intelligence AI command-line tools."""


@app.command()
def info() -> None:
    """Show the active configuration (secrets are never printed)."""
    settings = get_settings()
    rows: list[tuple[str, str]] = [
        ("version", __version__),
        ("data_dir", str(settings.data_dir.resolve())),
        ("default_symbol", settings.default_symbol),
        ("log_level", settings.log_level),
    ]
    for name in ("twelve_data_api_key", "oanda_api_token", "fred_api_key", "anthropic_api_key"):
        rows.append((name, "set" if getattr(settings, name) is not None else "not set"))

    width = max(len(label) for label, _ in rows) + 2
    for label, value in rows:
        typer.echo(f"{label + ':':<{width}}{value}")


if __name__ == "__main__":  # pragma: no cover
    app()
