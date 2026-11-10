from pathlib import Path

import pytest

from gold_intel.config import Settings


def test_defaults(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)  # ensure no stray .env is picked up
    settings = Settings()
    assert settings.default_symbol == "XAUUSD"
    assert settings.data_dir == Path("data")
    assert settings.raw_dir == Path("data") / "raw"
    assert settings.processed_dir == Path("data") / "processed"
    assert settings.twelve_data_api_key is None


def test_environment_overrides(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("GOLD_INTEL_DATA_DIR", str(tmp_path / "store"))
    monkeypatch.setenv("GOLD_INTEL_FRED_API_KEY", "abc123")
    settings = Settings()
    assert settings.data_dir == tmp_path / "store"
    assert settings.fred_api_key is not None
    assert settings.fred_api_key.get_secret_value() == "abc123"
    assert "abc123" not in repr(settings)


def test_reads_dotenv_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".env").write_text("GOLD_INTEL_DEFAULT_SYMBOL=EURUSD\n", encoding="utf-8")
    assert Settings().default_symbol == "EURUSD"
