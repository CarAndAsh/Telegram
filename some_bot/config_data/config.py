from dataclasses import dataclass

from environs import Env

from log_config import logger


@dataclass
class TGBot:
    token: str


@dataclass
class Config:
    tg_bot: TGBot


def load_config(path: str):
    env: Env = Env()
    env.read_env(path)
    logger.debug('чтение из файла конфигурации')
    return Config(tg_bot=TGBot(token=env('TOKEN')))
