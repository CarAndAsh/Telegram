from aiogram import Router
from aiogram.methods import SendMessage
from aiogram.types import Message

from bot_core.log_cofig import logger

other_router: Router = Router()


@other_router.message()
async def echo(msg: Message) -> SendMessage:
    if msg.text:
        logger.info(f'Поступило сообщение: {msg.text}')
        await msg.answer(msg.text)
