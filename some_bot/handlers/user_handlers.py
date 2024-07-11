from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from lexicon.lexicon import LEXICON_RU
from log_config import logger

user_router: Router = Router()

brn_1 = KeyboardButton(text=LEXICON_RU['btn_1'])
btn_2 = KeyboardButton(text=LEXICON_RU['btn_2'])
keyboard = ReplyKeyboardMarkup(keyboard=[[brn_1, btn_2]],
                               resize_keyboard=True,
                               one_time_keyboard=True)


async def process_start_command(msg: Message):
    logger.info('get command start')
    await msg.answer(text=LEXICON_RU['/start'], reply_markup=keyboard)


async def process_help_command(msg: Message):
    logger.info('get command help')
    await msg.answer(text=LEXICON_RU['/help'])


async def process_btn_command(msg: Message):
    logger.info('get any answer')
    await msg.answer(text=(LEXICON_RU['answer_1'] if msg.text == LEXICON_RU['btn_1'] else LEXICON_RU['answer_2']),
                     reply_markup=ReplyKeyboardRemove())


user_router.message.register(process_start_command, CommandStart())
user_router.message.register(process_help_command, Command(commands='help', prefix='/'))
user_router.message.register(process_btn_command, F.text.in_([LEXICON_RU['btn_1'], LEXICON_RU['btn_2']]))
