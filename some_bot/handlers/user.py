from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from .FSM import FSMFormAboutUser
from keyboards.keyboards import inline_kb
from lexicon.lexicon_ru import LEXICON_RU
from log_config import logger
from middlewares.outer import FSMMiddleware

user_router: Router = Router()
user_router.message.outer_middleware(FSMMiddleware())


async def start_command(msg: Message):
    logger.debug('User send start command')
    await msg.answer(text=LEXICON_RU['/start'].format(msg.from_user.first_name))


async def help_command(msg: Message):
    logger.debug('User send help command')
    await msg.answer(text=LEXICON_RU['/help'])


async def process_fill_form(msg: Message, state: FSMContext):
    await msg.answer('Отлично давай приступим. Выбери пол', reply_markup=inline_kb('gender'))
    await state.set_state(FSMFormAboutUser.choose_gender)
    logger.info(f'{msg.from_user.first_name} starts to fill form {state}')


async def process_cancel(msg: Message, state: FSMContext):
    await msg.answer('Хорошо, в следующий раз попробуем заполнить анкету полностью...',
                     reply_markup=ReplyKeyboardRemove())
    await state.clear()
    logger.info(f'{msg.from_user.first_name} interrupt fill form')


async def process_cancel_default(msg: Message):
    await msg.answer('Мы еще даже не начинали')
    logger.info(f'{msg.from_user.first_name} interrupt... what?!')


async def process_choose_gender(msg: Message, state: FSMContext):
    await msg.answer('Хоть я и знаю, но отправь мне свое имя...', reply_markup=ReplyKeyboardRemove())
    await state.update_data(gender=msg.text)
    await state.set_state(FSMFormAboutUser.fill_name)
    logger.info(f'{msg.from_user.first_name} goes to fill name')


async def process_fill_name(msg: Message, state: FSMContext):
    await msg.answer('А теперь фамилию')
    await state.update_data(first_name=msg.text)
    await state.set_state(FSMFormAboutUser.fill_second_name)
    logger.info(f'{msg.from_user.first_name} goes to fill second name')


async def process_fill_second_name(msg: Message, state: FSMContext):
    await msg.answer('Мне можешь доверить свой возраст')
    await state.update_data(second_name=msg.text)
    await state.set_state(FSMFormAboutUser.fill_age)
    logger.info(f'{msg.from_user.first_name} goes to fill age')


async def process_fill_age(msg: Message, state: FSMContext):
    await msg.answer('Выбери уровень своего образования', reply_markup=inline_kb('edu'))
    await state.update_data(age=msg.text)
    await state.set_state(FSMFormAboutUser.fill_education)
    logger.info(f'{msg.from_user.first_name} goes to fill education')


async def process_fill_education(msg: Message, state: FSMContext):
    await msg.answer('Дай я на тебя посмотрю (скинь свое фото)', reply_markup=ReplyKeyboardRemove())
    await state.update_data(education=msg.text)
    await state.set_state(FSMFormAboutUser.upload_photo)
    logger.info(f'{msg.from_user.first_name} goes to upload photo')


async def process_upload_photo(msg: Message, state: FSMContext):
    await msg.answer('Замечательно!')
    await state.update_data(photo=msg.photo)
    await state.clear()
    logger.info(f'{msg.from_user.first_name} complete fill form!')


user_router.message.register(start_command, CommandStart(), StateFilter(default_state))
user_router.message.register(help_command, Command(commands='help', prefix='/'))
user_router.message.register(process_fill_form, Command(commands='fill_form', prefix='/'), StateFilter(default_state))
user_router.message.register(process_cancel, Command(commands='cancel', prefix='/'), ~StateFilter(default_state))
user_router.message.register(process_cancel_default, Command(commands='cancel', prefix='/'), StateFilter(default_state))
user_router.message.register(process_choose_gender, StateFilter(FSMFormAboutUser.choose_gender))
user_router.message.register(process_fill_name, StateFilter(FSMFormAboutUser.fill_name))
user_router.message.register(process_fill_second_name, StateFilter(FSMFormAboutUser.fill_second_name))
user_router.message.register(process_fill_age, StateFilter(FSMFormAboutUser.fill_age))
user_router.message.register(process_fill_education, StateFilter(FSMFormAboutUser.fill_education))
user_router.message.register(process_upload_photo, StateFilter(FSMFormAboutUser.upload_photo))
