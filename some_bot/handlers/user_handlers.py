from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import CommandStart, Command

from log_cofig import logger
from lexicon.lexicon import LEXICON_RU, LEXICON_KB
from keyboards.in_line import in_line_kb
from services.services import edit_image

user_router = Router()


async def process_start(msg: Message):
    user_full_name = msg.from_user.full_name
    logger.info(f'{user_full_name} start work with bot')
    await msg.answer(LEXICON_RU[msg.text].format(user_full_name))


async def process_help(msg: Message):
    logger.info(f'{msg.from_user.full_name} ask help info from bot')
    await msg.answer(LEXICON_RU[msg.text], reply_markup=in_line_kb())


async def process_image(msg: Message):
    logger.info(f'bot get image')
    pic_id = msg.photo[-1].file_id
    await msg.answer_photo(pic_id, caption='Это ваше фото.\n Что бы вы хотели с ним сделать?',
                           reply_markup=in_line_kb())


async def process_our_callback(callback: CallbackQuery):
    logger.info('bot get our callback')
    pic_id = callback.message.photo[-1].file_id
    await callback.message.edit_media(media=InputMediaPhoto(media=edit_image(pic_id, int(callback.data[-1])),
                                                            caption=f'Вы использовали {LEXICON_KB[callback.data]}'),
                                      reply_markup=in_line_kb()
                                      )

user_router.message.register(process_start, CommandStart())
user_router.message.register(process_help, Command(commands='help', prefix='/'))
user_router.message.register(process_image, F.photo)
user_router.callback_query.register(process_our_callback, F.data.in_(LEXICON_KB))
