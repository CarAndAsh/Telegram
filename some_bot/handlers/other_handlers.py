from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU
from log_config import logger

other_router: Router = Router()


async def process_other_answer(msg: Message):
    logger.info(f'get message: {msg.text}')
    await msg.reply(LEXICON_RU['other'])


other_router.message.register(process_other_answer, )
