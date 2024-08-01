from aiogram import Router
from aiogram.types import Message

from filters.filters import MyFalseFilter, MyTrueFilter
from lexicon.lexicon_ru import LEXICON_RU
from log_config import logger

other_router: Router = Router()


@other_router.message()
async def other_answer(msg: Message):
    logger.debug('Enter echo')
    try:
        await msg.send_copy(chat_id=msg.chat.id)
    except TypeError:
        await msg.reply(text=LEXICON_RU['other'])
    logger.debug('Exit echo')
