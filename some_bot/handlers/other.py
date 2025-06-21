from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from log_config import logger

other_router = Router()


async def echo(msg: Message):
    logger.info(f'бот получил сообщение: {msg.text}')
    await msg.answer(msg.text)


async def process_other_callback(callback: CallbackQuery):
    logger.info(f'{callback.from_user.full_name} что-то делает не так')
    await callback.answer()

other_router.message.register(echo, )
other_router.callback_query.register(process_other_callback, )
