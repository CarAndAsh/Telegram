from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from log_config import logger

other_router: Router = Router()


@other_router.message()
async def other_answer(msg: Message):
    await msg.answer(text=LEXICON_RU['other'])
    logger.debug(f"{msg.from_user.first_name} message doesn't match question in form")
