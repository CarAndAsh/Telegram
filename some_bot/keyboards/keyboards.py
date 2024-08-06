from aiogram.utils.keyboard import (ReplyKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup)
from lexicon.lexicon_ru import LEXICON_KB_RU


def inline_kb(kb: str) -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(*[KeyboardButton(text=LEXICON_KB_RU[kb][btn], callback_data=btn) for btn in LEXICON_KB_RU[kb]])
    keyboard: ReplyKeyboardMarkup = kb_builder.as_markup()
    keyboard.resize_keyboard = True
    return keyboard
