from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from log_cofig import logger

BASE_DIR = Path(__file__).resolve().parent.parent


class LogSettings(BaseModel):
    pass


class TGBotSettings(BaseModel):
    token: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env',
        env_nested_delimiter='-',
        case_sensitive=False,
        extra='ignore'
    )
    tg_bot: TGBotSettings


settings = Settings()
