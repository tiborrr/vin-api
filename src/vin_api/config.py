from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database Settings
    database_url: str = "postgresql+psycopg://vpic:vpic_password@127.0.0.1:5434/vpic_db"
    
    # Scraper & Docker Update Settings
    postgres_host: str = "127.0.0.1"
    postgres_port: int = 5434
    postgres_password: str = "vpic_password"
    postgres_user: str = "vpic"
    postgres_db: str = "vpic_db"
    db_update_interval_seconds: int = 86400

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore", frozen=True)


@lru_cache
def get_settings() -> Settings:
    """
    Dependency injection for settings.
    Uses lru_cache to ensure the Settings object is instantiated only once.
    """
    return Settings()
