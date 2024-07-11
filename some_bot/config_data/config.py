from dataclasses import dataclass
from environs import Env


@dataclass
class TGBot:
    token: str


@dataclass
class Config:
    tg_bot: TGBot


def load_config(path: str):
    env: Env = Env()
    env.read_env(path)
    return Config(tg_bot=TGBot(token=env('TOKEN')))