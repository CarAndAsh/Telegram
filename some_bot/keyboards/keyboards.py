from aiogram.utils.keyboard import (ReplyKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup)


def in_line_kb() -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(*[KeyboardButton(text=f'{btn + 1}', callback_data=str(btn)) for btn in range(4)])
    return kb_builder.as_markup()