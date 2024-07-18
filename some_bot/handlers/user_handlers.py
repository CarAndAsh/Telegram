from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

from lexicon.lexicon_ru import LEXICON_RU, LEXICON_KB_RU
from keyboards.keyboards import yn_keyboard, game_keyboard
from services.services import get_bot_choice, get_winner
from log_config import logger

user_router: Router = Router()


async def start_command(msg: Message):
    logger.debug('Player send start command')
    await msg.answer(text=LEXICON_RU['/start'], reply_markup=yn_keyboard, parse_mode=ParseMode.HTML)


async def help_command(msg: Message):
    logger.debug('Player send help command')
    await msg.answer(text=LEXICON_RU['/help'], reply_markup=yn_keyboard, parse_mode=ParseMode.HTML)


async def agree_btn(callb: CallbackQuery):
    logger.debug('Player push button for agree')
    await callb.message.edit_text(text=LEXICON_RU[callb.data], reply_markup=game_keyboard)


async def disagree_btn(callb: CallbackQuery):
    logger.debug('Player push button for disagree')
    await callb.message.edit_text(text=LEXICON_RU[callb.data], reply_markup=yn_keyboard)


async def game_btn(callb: CallbackQuery):
    bot_choice = get_bot_choice()
    logger.debug(f'Player made his choise. {callb.data} goes to check winner')
    winner = get_winner(callb.data, bot_choice)
    await callb.message.edit_text(text=f'{LEXICON_RU["bot_choice"]}{LEXICON_KB_RU[bot_choice]}\n\n{LEXICON_RU[winner]}',
                                  reply_markup=yn_keyboard)


user_router.message.register(start_command, CommandStart())
user_router.message.register(help_command, Command(commands='help', prefix='/'))
user_router.callback_query.register(agree_btn, F.data == 'agree')
user_router.callback_query.register(disagree_btn, F.data.in_(('disagree', 'remind')))
user_router.callback_query.register(game_btn, F.data.in_(LEXICON_KB_RU.keys()))
