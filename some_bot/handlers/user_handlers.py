from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU
from log_config import logger

user_router: Router = Router()

btn_list = (KeyboardButton(text=btn) for btn in LEXICON_RU['btn_tpl'])
kb_builder = ReplyKeyboardBuilder()
kb_builder.row(*btn_list, width=3)


async def process_start_command(msg: Message):
    logger.info('get command start')
    await msg.answer(text=''.join(LEXICON_RU['/start']), reply_markup=kb_builder.as_markup(resize_keyboard=True))


async def process_help_command(msg: Message):
    logger.info('get command help')
    await msg.answer(text=LEXICON_RU['/help'])


async def process_btn_command(msg: Message):
    logger.info('get any answer')
    await msg.answer(text=(LEXICON_RU['answer_tpl'][LEXICON_RU['btn_tpl'].index(msg.text)]))
    await msg.answer(text=LEXICON_RU['/start'][1])


user_router.message.register(process_start_command, CommandStart())
user_router.message.register(process_help_command, Command(commands='help', prefix='/'))
user_router.message.register(process_btn_command, F.text.in_(LEXICON_RU['btn_tpl']))
