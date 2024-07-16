from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU, LEXICON_KB_RU
from services.services import RULES

"""Here realized both variants of keyboard(with builder and without it)"""


def generate_keyboard(width: int, *args, **kwargs) -> ReplyKeyboardMarkup:
    kbb = ReplyKeyboardBuilder()
    btn_list: List[KeyboardButton] = []
    if args:
        btn_list = [KeyboardButton(text=LEXICON_KB_RU.get(btn, btn)) for btn in args]
    if kwargs:
        btn_list = [KeyboardButton(text=text) for btn, text in kwargs]
    kbb.row(*btn_list, width=width)
    return kbb.as_markup()


# keyboard without builder
yes_btn = KeyboardButton(text=LEXICON_KB_RU['yes'])
no_btn = KeyboardButton(text=LEXICON_KB_RU['no'])

yn_keyboard = ReplyKeyboardMarkup(keyboard=[[yes_btn], [no_btn]], one_time_keyboard=True, resize_keyboard=True)

# keyboard with builder

game_keyboard: ReplyKeyboardMarkup = generate_keyboard(3, *(*RULES,'remind'))
game_keyboard.resize_keyboard = True