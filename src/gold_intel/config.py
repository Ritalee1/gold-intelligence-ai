"""Application settings.

Values are read from environment variables prefixed with ``GOLD_INTEL_`` and from a
local ``.env`` file (git-ignored). Secrets such as API keys must never be committed.
"""

from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration for Gold Intelligence AI."""

    model_config = SettingsConfigDict(
        env_prefix="GOLD_INTEL_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    data_dir: Path = Path("data")
    log_level: str = "INFO"
    default_symbol: str = "XAUUSD"

    # Provider credentials (optional until the relevant adapter is used).
    twelve_data_api_key: SecretStr | None = None
    oanda_api_token: SecretStr | None = None
    fred_api_key: SecretStr | None = None
    anthropic_api_key: SecretStr | None = None

    @property
    def raw_dir(self) -> Path:
        """Directory for untouched provider downloads."""
        return self.data_dir / "raw"

    @property
    def processed_dir(self) -> Path:
        """Directory for validated, normalised Parquet datasets."""
        return self.data_dir / "processed"


@lru_cache
def get_settings() -> Settings:
    """Return the cached application settings."""
    return Settings()
