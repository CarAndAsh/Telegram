from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config import load_config
from log_cofig import logger

config = load_config('./.env')
logger.info('config loads')
bot = Bot(config.tg_bot.token)
dp = Dispatcher()


async def echo(msg: Message):
    logger.info(f'bot get message: {msg.text}')
    await msg.answer(msg.text)


dp.message.register(echo)
if __name__ == '__main__':
    logger.debug('bot is running')
    dp.run_polling(bot)
