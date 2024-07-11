from aiogram import Bot, Dispatcher
from asyncio import run

from config_data.config import load_config, Config
from handlers import user_handlers, other_handlers


async def main_func():
    config: Config = load_config('./.env')
    echo_bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(user_handlers.user_router)
    dp.include_router(other_handlers.other_router)

    await echo_bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(echo_bot)

run(main_func())
