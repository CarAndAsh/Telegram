from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_KB_RU, LEXICON_RU
from services.services import RULES

"""Here realized both variants of keyboard(with builder and without it)"""


def generate_keyboard(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    kbb = InlineKeyboardBuilder()
    btn_list: List[InlineKeyboardButton] = []
    if args:
        btn_list = [InlineKeyboardButton(text=LEXICON_KB_RU.get(btn, btn), callback_data=btn) for btn in args]
    if kwargs:
        btn_list = [InlineKeyboardButton(text=text, callback_data=btn) for btn, text in kwargs]
    kbb.row(*btn_list, width=width)
    return kbb.as_markup()


# keyboard without builder
yes_btn = InlineKeyboardButton(text=LEXICON_KB_RU['yes'], callback_data='agree')
no_btn = InlineKeyboardButton(text=LEXICON_KB_RU['no'], callback_data='disagree')

yn_keyboard = InlineKeyboardMarkup(inline_keyboard=[[yes_btn], [no_btn]])

# keyboard with builder

game_keyboard: InlineKeyboardMarkup = generate_keyboard(2, *(*RULES, 'remind'))
