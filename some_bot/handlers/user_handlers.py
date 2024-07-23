from copy import deepcopy
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from database.database import user_dict_template, users_db
from filters.filters import IsDigitCallbackData, IsDelBookmarkCallbackData
from keyboards.bookmarks_kb import build_bookmarks_kb, build_bookmarks_edit_kb
from keyboards.pagination import build_pagination_kb
from services.file_handling import book
from lexicon.lexicon_ru import LEXICON_RU
from log_config import logger

user_router: Router = Router()


async def start_command(msg: Message):
    logger.debug('Player send start command')
    await msg.answer(text=LEXICON_RU['/start'])
    if msg.from_user.id not in users_db:
        users_db[msg.from_user.id] = deepcopy(user_dict_template)


async def help_command(msg: Message):
    logger.debug('Player send help command')
    await msg.answer(text=LEXICON_RU['/help'])


async def beginning_command(msg: Message):
    users_db[msg.from_user.id]['page'] = 1
    text = book[users_db[msg.from_user.id]['page']]
    await msg.answer(
        text=text,
        reply_markup=build_pagination_kb(
            'backward',
            f'{users_db[msg.from_user.id]["page"]}/{len(book)}',
            'forward'
        )
    )


async def continue_command(msg: Message):
    text = book[users_db[msg.from_user.id]['page']]
    await msg.answer(
        text=text,
        reply_markup=build_pagination_kb(
            'backward',
            f'{users_db[msg.from_user.id]["page"]}/{len(book)}',
            'forward'
        )
    )


async def bookmarks_command(msg: Message):
    page_num_set = users_db[msg.from_user.id]['bookmarks']
    if page_num_set:
        await msg.answer(text=LEXICON_RU[msg.text], reply_markup=build_bookmarks_kb(*page_num_set))
    else:
        await msg.answer(text=LEXICON_RU['no_bookmarks'])


async def forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] < len(book):
        users_db[callback.from_user.id]['page'] += 1
        text = book[users_db[callback.from_user.id]['page']]
        await callback.message.edit_text(text=text,
                                         reply_markup=build_pagination_kb(
                                             'backward',
                                             f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                                             'forward'))
    else:
        await callback.answer()


async def backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] > 1:
        users_db[callback.from_user.id]['page'] -= 1
        text = book[users_db[callback.from_user.id]['page']]
        await callback.message.edit_text(text=text,
                                         reply_markup=build_pagination_kb(
                                             'backward',
                                             f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                                             'forward'))
    else:
        await callback.answer()


async def page_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].add(users_db[callback.from_user.id]['page'])
    await callback.answer('Страница добавлена в закладки')


async def bookmark_press(callback: CallbackQuery):
    text = book[int(callback.data)]
    users_db[callback.from_user.id]['page'] = int(callback.data)
    await callback.message.edit_text(text=text,
                                     reply_markup=build_pagination_kb(
                                         'backward',
                                         f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                                         'forward'))


async def edit_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU[callback.data],
                                     reply_markup=build_bookmarks_edit_kb(
                                         *users_db[callback.from_user.id]['bookmarks']))


async def cancel_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['cancel_text'])


async def del_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].remove(int(callback.data[:-3]))
    if users_db[callback.from_user.id]['bookmarks']:
        await callback.message.edit_text(text=LEXICON_RU['/bookmarks'],
                                         reply_markup=build_bookmarks_edit_kb(*users_db[callback.from_user.id]['bookmarks']))
    else:
        await callback.message.edit_text(text=LEXICON_RU['no_bookmarks'])

user_router.message.register(start_command, CommandStart())
user_router.message.register(help_command, Command(commands='help', prefix='/'))
user_router.message.register(beginning_command, Command(commands='beginning', prefix='/'))
user_router.message.register(continue_command, Command(commands='continue', prefix='/'))
user_router.message.register(bookmarks_command, Command(commands='bookmarks', prefix='/'))
user_router.callback_query.register(forward_press, F.data == 'forward')
user_router.callback_query.register(backward_press, F.data == 'backward')
user_router.callback_query.register(page_press, lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
user_router.callback_query.register(bookmark_press, IsDigitCallbackData())
user_router.callback_query.register(edit_press, F.data == 'edit_bookmarks')
user_router.callback_query.register(cancel_press, F.data == 'cancel')
user_router.callback_query.register(del_press, IsDelBookmarkCallbackData())
