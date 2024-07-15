from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from asyncio import run

from config_data.config import load_config, Config
from handlers import user_handlers, other_handlers
from keyboards.menu_comands import set_menu

from log_config import logger


# TODO multiplayer between two and more players
# TODO get name of users for logs


async def main_func():
    config: Config = load_config('./.env')
    game_bot = Bot(config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    desc = 'Этот бот для игры в "Камень, ножницы, бумага, ящерица, Спок".'
    name = 'Бот "Камень, ножницы, бумага, ящерица, Спок"'
    dp.include_router(user_handlers.user_router)
    dp.include_router(other_handlers.other_router)
    logger.info('Start bot')
    await game_bot.set_my_description(description=desc)
    await game_bot.set_my_name(name=name)
    await game_bot.delete_webhook(drop_pending_updates=True)
    await set_menu(game_bot)
    await dp.start_polling(game_bot)


run(main_func())
