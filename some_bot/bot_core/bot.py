from aiogram import Bot, Dispatcher

from bot_core.config import settings
from handlers import router
from lexicon.lexicon_ru import BOT_INFO


async def name_and_desc_check_and_set(bot: Bot):
    bot_name = await bot.get_my_name()
    bot_short_desc = await bot.get_my_short_description()
    bot_desc = await bot.get_my_description()
    if bot_name != (name := BOT_INFO['name']):
        await bot.set_my_name(name)
    if bot_short_desc != (short_desc := BOT_INFO['short_desc']):
        await bot.set_my_short_description(short_desc)
    if bot_desc != (desc := BOT_INFO['desc']):
        await bot.set_my_description(desc)


def create_bot() -> Bot:
    bot = Bot(settings.tg_bot.token)
    return bot


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(router)
    return dp
