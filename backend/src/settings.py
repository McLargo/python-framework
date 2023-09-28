
import logging

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Python framework"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
