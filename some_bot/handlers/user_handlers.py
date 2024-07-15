from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import yn_keyboard, game_keyboard
from services.services import get_bot_choice, get_winner
from log_config import logger

user_router: Router = Router()


async def start_command(msg: Message):
    logger.debug('Player send start command')
    await msg.answer(text=LEXICON_RU['/start'], reply_markup=yn_keyboard)


async def help_command(msg: Message):
    logger.debug('Player send help command')
    await msg.answer(text=LEXICON_RU['/help'], reply_markup=yn_keyboard)


async def agree_btn(msg: Message):
    logger.debug('Player push button for agree')
    await msg.answer(text=LEXICON_RU['yes'], reply_markup=game_keyboard)


async def disagree_btn(msg: Message):
    logger.debug('Player push button for disagree')
    await msg.answer(text=LEXICON_RU['disagree'], reply_markup=ReplyKeyboardRemove())


async def game_btn(msg: Message):
    bot_choice = get_bot_choice()
    logger.debug('Player made his choise')
    await msg.answer(text=f'{LEXICON_RU["bot_choice"]} {LEXICON_RU[bot_choice]}')
    winner = get_winner(msg.text, bot_choice)
    await msg.answer(text=LEXICON_RU[winner], reply_markup=yn_keyboard)


user_router.message.register(start_command, CommandStart())
user_router.message.register(help_command, Command(commands='help', prefix='/'))
user_router.message.register(agree_btn, F.text == LEXICON_RU['yes'])
user_router.message.register(disagree_btn, F.text.in_((LEXICON_RU['no'], LEXICON_RU['remind'])))
user_router.message.register(game_btn, F.text.in_(
    (LEXICON_RU['rock'], LEXICON_RU['scissors'], LEXICON_RU['paper'], LEXICON_RU['lizard'], LEXICON_RU['spock'])))
