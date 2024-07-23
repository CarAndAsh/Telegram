from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU


def build_pagination_kb(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(text=LEXICON_RU[btn] if btn in LEXICON_RU else btn, callback_data=btn) for btn in buttons])
    return kb_builder.as_markup()
