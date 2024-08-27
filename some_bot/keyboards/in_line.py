from aiogram.utils.keyboard import (InlineKeyboardButton, InlineKeyboardMarkup, InlineKeyboardBuilder)

from lexicon.lexicon_ru import LEXICON_KB


def in_line_kb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(text=LEXICON_KB[btn], callback_data=btn) for btn in LEXICON_KB])
    kb_builder.adjust(2, 2, 1, 1, 1)
    return kb_builder.as_markup()
