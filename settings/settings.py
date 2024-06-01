from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    clickhouse_host: str
    clickhouse_port: int

    model_config = SettingsConfigDict(
        env
    )