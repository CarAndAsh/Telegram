from asyncio import run

from bot_core.bot import create_bot, create_dispatcher, name_and_desc_check_and_set
from bot_core.log_cofig import logger

logger.name = __file__

async def main():
    bot = create_bot()
    # await name_and_desc_check_and_set(bot)
    logger.info('Конфигурация загружена')
    dp = create_dispatcher()
    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot)

#
# if __name__ == '__main__':
#     logger.debug('Бот запущен')
#     run(main())
