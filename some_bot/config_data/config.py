from dataclasses import dataclass
from environs import Env
from log_cofig import logger


@dataclass
class TGBot:
    token: str


@dataclass
class Config:
    tg_bot: TGBot


def load_config(path: str):
    env: Env = Env()
    env.read_env(path)
    logger.debug('read config from file')
    return Config(tg_bot=TGBot(token=env('TOKEN')))