from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from backend.settings.path import BasePath


class Settings(BaseSettings):
    clickhouse_host: str
    clickhouse_port: int
    clickhouse_table: str
    embedding_model: str
    chatbot_model: str

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        env_file=f"{BasePath}/.env",
        extra="ignore",
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()
