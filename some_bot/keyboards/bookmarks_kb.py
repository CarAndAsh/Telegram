from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU
from services.file_handling import book


def build_bookmarks_kb(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    for btn in sorted(args):
        kb_builder.row(InlineKeyboardButton(text=f'{btn} - {book[btn][:100]}',
                                            callback_data=str(btn)))
    kb_builder.row(InlineKeyboardButton(text=LEXICON_RU['edit_bookmarks_btn'], callback_data='edit_bookmarks'),
                   InlineKeyboardButton(text=LEXICON_RU['cancel'], callback_data='cancel'))
    return kb_builder.as_markup()


def build_bookmarks_edit_kb(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    for btn in sorted(args):
        kb_builder.row(InlineKeyboardButton(text=f'{LEXICON_RU["del"]} {btn} - {book[btn][:100]}',
                                            callback_data=f'{btn}del'))
    kb_builder.row(InlineKeyboardButton(text=LEXICON_RU['cancel'], callback_data='cancel'))
    return kb_builder.as_markup()
