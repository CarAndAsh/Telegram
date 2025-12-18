from aiogram import Bot, Dispatcher
from aiogram.types import Message

from bot_core.config import settings
from bot_core.log_cofig import logger

logger.name = __file__
bot = Bot(settings.tg_bot.token)
logger.info('Конфигурация загружена')
dp = Dispatcher()


async def echo(msg: Message):
    if msg.text:
        logger.info(f'Поступило сообщение: {msg.text}')
        await msg.answer(msg.text)


dp.message.register(echo)
if __name__ == '__main__':
    logger.debug('Бот запущен')
    dp.run_polling(bot)
