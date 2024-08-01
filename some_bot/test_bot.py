from aiogram import Bot, Dispatcher

from handlers.user_handlers import user_router
from handlers.other_handlers import other_router
from config_data.config import load_config
from log_cofig import logger

"""
1. Process updates with Image or File
2. Ignore (m.b. with message-answer) other types of Updates
3. Image in preview message with comment about last done operation. And with in-line keyboard with operations
"""

config = load_config('./.env')
logger.info('config loads')
bot = Bot(config.tg_bot.token)
dp = Dispatcher()
dp.include_routers(user_router, other_router)

if __name__ == '__main__':
    logger.debug('bot is running')
    dp.run_polling(bot)
