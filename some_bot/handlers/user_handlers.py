from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU
from log_config import logger

user_router: Router = Router()


async def process_start_command(msg: Message):
    logger.info('get command start')
    await msg.answer(text=LEXICON_RU['/start'])


async def process_help_command(msg: Message):
    logger.info('get command help')
    await msg.answer(text=LEXICON_RU['/help'])


user_router.message.register(process_start_command, CommandStart())
user_router.message.register(process_help_command, Command(commands='help', prefix='/'))
