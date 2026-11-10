import pytest
from typer.testing import CliRunner

from gold_intel import __version__
from gold_intel.cli import app
from gold_intel.config import get_settings

runner = CliRunner()


@pytest.fixture(autouse=True)
def _clear_settings_cache() -> None:
    get_settings.cache_clear()


def test_version_flag_prints_version() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert result.output.strip() == f"gold-intel {__version__}"


def test_no_args_shows_help() -> None:
    result = runner.invoke(app, [])
    assert "Usage" in result.output


def test_info_never_prints_secret_values(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GOLD_INTEL_TWELVE_DATA_API_KEY", "super-secret-value")
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    lines = dict(line.split(":", 1) for line in result.output.splitlines())
    assert lines["twelve_data_api_key"].strip() == "set"
    assert lines["fred_api_key"].strip() == "not set"
    assert "super-secret-value" not in result.output


def test_python_dash_m_entry_point() -> None:
    import subprocess
    import sys

    result = subprocess.run(
        [sys.executable, "-m", "gold_intel", "--version"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == f"gold-intel {__version__}"
