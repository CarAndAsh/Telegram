from asyncio import run
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import load_config, Config
from handlers.user import user_router
from handlers.other import other_router
from menu.menu import set_menu
from lexicon.lexicon_ru import LEXICON_FACE_BOT_RU
from log_config import logger


# TODO Missing updates must go into other_router


async def main_func():
    config: Config = load_config('./.env')
    test_bot = Bot(config.tg_bot.token)

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(user_router)
    dp.include_router(other_router)
    dp.startup.register(set_menu)

    bot_name = await test_bot.get_my_name()
    bot_short_desc = await test_bot.get_my_short_description()
    bot_desc = await test_bot.get_my_description()
    logger.info('Start bot')
    if bot_name.name != LEXICON_FACE_BOT_RU['name']:
        await test_bot.set_my_name(name=LEXICON_FACE_BOT_RU['name'])
    if bot_short_desc.short_description != LEXICON_FACE_BOT_RU['short_desc']:
        await test_bot.set_my_short_description(short_description=LEXICON_FACE_BOT_RU['short_desc'])
    if bot_desc.description != LEXICON_FACE_BOT_RU['desc']:
        await test_bot.set_my_description(description=LEXICON_FACE_BOT_RU['desc'])

    await test_bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(test_bot, polling_timeout=40)


run(main_func())
