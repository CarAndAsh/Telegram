from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from asyncio import run

from config_data.config import load_config, Config
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_menu

from log_config import logger


# TODO get name of users for logs
# TODO adding books
# TODO try int bookmark callback (because str to int and then int to str)
# TODO correct work of _get_part_text func


async def main_func():
    config: Config = load_config('./.env')
    book_bot = Bot(config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    desc = 'Этот бот для чтения книг...".'
    name = 'Бот-читалка'
    dp.include_router(user_handlers.user_router)
    dp.include_router(other_handlers.other_router)
    logger.info('Start bot')
    if book_bot.get_my_description() != desc:
        await book_bot.set_my_description(description=desc)
    if book_bot.get_my_name() != name:
        await book_bot.set_my_name(name=name)
    await set_menu(book_bot)
    await book_bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(book_bot)


run(main_func())
