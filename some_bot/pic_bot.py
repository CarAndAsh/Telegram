from asyncio import run
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import load_config
from handlers.user import user_router
from handlers.other import other_router
from lexicon.lexicon_ru import LEXICON_FACE_BOT_RU
from log_config import logger

"""
1. Process updates with Image or File
2. Ignore (m.b. with message-answer) other types of Updates
3. Image in preview message with comment about last done operation. And with in-line keyboard with operations
"""

config = load_config('./.env')
logger.info('config loads')
pic_bot = Bot(config.tg_bot.token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_router(user_router)
dp.include_router(other_router)


async def main_func():
    bot_name = await pic_bot.get_my_name()
    bot_short_desc = await pic_bot.get_my_short_description()
    bot_desc = await pic_bot.get_my_description()
    logger.info('Start bot')
    if bot_name.name != LEXICON_FACE_BOT_RU['name']:
        await pic_bot.set_my_name(name=LEXICON_FACE_BOT_RU['name'])
    if bot_short_desc.short_description != LEXICON_FACE_BOT_RU['short_desc']:
        await pic_bot.set_my_short_description(short_description=LEXICON_FACE_BOT_RU['short_desc'])
    if bot_desc.description != LEXICON_FACE_BOT_RU['desc']:
        await pic_bot.set_my_description(description=LEXICON_FACE_BOT_RU['desc'])
    logger.debug('bot is running')
    await pic_bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(pic_bot)


if __name__ == '__main__':
    run(main_func())
