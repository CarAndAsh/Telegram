from aiogram import Bot, Dispatcher
from aiogram.types import Message

from bot_core.config import settings
from bot_core.log_cofig import logger

logger.info('config loads')
bot = Bot(settings.tg_bot.token)
dp = Dispatcher()


async def echo(msg: Message):
    logger.info(f'bot get message: {msg.text}')
    await msg.answer(msg.text)


dp.message.register(echo)
if __name__ == '__main__':
    logger.debug('bot is running')
    dp.run_polling(bot)
