from asyncio import run

from aiogram import Bot, Dispatcher

from bot_core.config import settings
from bot_core.log_cofig import logger
from handlers.other import other_router

logger.name = __file__

async def main():
    bot = Bot(settings.tg_bot.token)
    logger.info('Конфигурация загружена')
    dp = Dispatcher()

    dp.include_router(other_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logger.debug('Бот запущен')
    run(main())