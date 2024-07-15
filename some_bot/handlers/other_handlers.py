from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from log_config import logger

other_router: Router = Router()


async def other_answer(msg: Message):
    logger.debug('player send something...')
    await msg.reply(text=LEXICON_RU['other'])


other_router.message.register(other_answer, )
