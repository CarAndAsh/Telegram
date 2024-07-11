from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU
from log_config import logger

other_router: Router = Router()


async def echo(msg: Message):
    logger.info(f'get message: {msg.text}')
    try:
        await msg.send_copy(chat_id=msg.chat.id)
    except TypeError:
        await msg.reply(LEXICON_RU['no_echo'])


other_router.message.register(echo, )
