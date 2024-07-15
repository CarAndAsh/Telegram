from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU
from services.services import RULES

"""Here realized both variants of keyboard(with builder and without it)"""

# keyboard without builder
yes_btn = KeyboardButton(text=LEXICON_RU['yes'])
no_btn = KeyboardButton(text=LEXICON_RU['no'])

yn_keyboard = ReplyKeyboardMarkup(keyboard=[[yes_btn], [no_btn]], one_time_keyboard=True, resize_keyboard=True)

# keyboard with builder
game_kb_builder = ReplyKeyboardBuilder()

game_kb_builder.row(*(KeyboardButton(text=LEXICON_RU[i]) for i in (*RULES, 'remind')), width=3)
game_keyboard: ReplyKeyboardMarkup = game_kb_builder.as_markup(resize_keyboard=True)
