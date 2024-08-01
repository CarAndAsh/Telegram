from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon_ru import LEXICON_RU
from log_config import logger
from keyboards.keyboards import in_line_kb


user_router: Router = Router()


async def start_command(msg: Message):
    logger.debug('User send start command')
    keyboard = in_line_kb()
    keyboard.resize_keyboard = True
    await msg.answer(text=LEXICON_RU['/start'].format(msg.from_user.first_name), reply_markup=keyboard)


async def help_command(msg: Message):
    logger.debug('User send help command')
    keyboard = in_line_kb()
    keyboard.resize_keyboard = True
    await msg.answer(text=LEXICON_RU['/help'],  reply_markup=keyboard)


async def process_callback(callback: CallbackQuery):
    text = callback.data
    logger.debug(f'User send callback with {text}')
    if callback.message.text == text:
        await callback.answer()
    else:
        await callback.message.edit_text(f'Ты нажал {int(text) + 1}')

user_router.message.register(start_command, CommandStart())
user_router.message.register(help_command, Command(commands='help', prefix='/'))
user_router.callback_query.register(process_callback,)