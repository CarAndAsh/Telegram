from aiogram import Bot, Dispatcher

from bot_core.config import settings
from handlers import router


def create_bot() -> Bot:
    bot = Bot(settings.tg_bot.token)
    return bot

def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(router)
    return dp