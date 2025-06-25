from io import BytesIO

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, BufferedInputFile

from handlers.FSM import FSMImageEditor
from keyboards.in_line import in_line_kb
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_KB
from log_config import logger
from services.services import get_mode_edit_image

user_router = Router()


async def process_start(msg: Message):
    user_full_name = msg.from_user.full_name
    logger.info(f'{user_full_name} начинает работу с ботом')
    await msg.answer(LEXICON_RU[msg.text].format(user_full_name))


async def process_help(msg: Message):
    logger.info(f'{msg.from_user.full_name} запрашивает справочную инфу по боту')
    await msg.answer(LEXICON_RU[msg.text])


async def get_imagefile(msg: Message, state: FSMContext, bot: Bot):
    logger.info(f'бот получил изображение как файл')
    state_data = {}
    doc_id = msg.document.file_id if msg.document else msg.photo[-1].file_id
    user_image = await bot.get_file(doc_id)
    path = user_image.file_path

    state_data['user_file_bin'] = BytesIO()
    state_data['path'] = path
    state_data['file_name'] = path.split('/')[-1]
    await bot.download_file(path, destination=state_data['user_file_bin'])
    await state.update_data(state_data)
    await msg.answer_photo(
        photo=BufferedInputFile(state_data['user_file_bin'].read1(), path),
        caption=f'я получил от тебя файл {path.split("/")[-1]}',
        reply_markup=in_line_kb()
    )
    await state.set_state(FSMImageEditor.edit_image)


async def send_edited_imagefile(callback: CallbackQuery, state: FSMContext):
    logger.info('bot sent editted image file')
    state_data = await state.get_data()
    state_data['user_file_bin'].seek(0)
    file_name = 'edited_' + state_data['file_name']
    await callback.message.answer_document(
        document=BufferedInputFile(state_data['user_file_bin'].read1(),
                                   filename=file_name),
        caption=f'Ищите файл c именем {file_name} в папке Telegram Desktop'
    )


async def end_editing_imagefile(callback: CallbackQuery, state: FSMContext):
    # TODO deleting and user message with orig image
    await callback.message.delete()
    await state.clear()


async def process_imagefile(callback: CallbackQuery, state: FSMContext):
    logger.info('bot get our callback')
    state_data = await state.get_data()
    pic_mode = get_mode_edit_image(state_data['user_file_bin'], callback.data)
    state_data['user_file_bin'].seek(0)
    await state.update_data(state_data)
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=BufferedInputFile(state_data['user_file_bin'].read1(), ''),
            caption=f'я подменил фото, цвет.схема {pic_mode}'),
        reply_markup=in_line_kb())


user_router.message.register(process_start, CommandStart())
user_router.message.register(process_help, Command(commands='help', prefix='/'))
user_router.message.register(get_imagefile, F.photo, StateFilter(default_state))
user_router.message.register(get_imagefile, F.document, StateFilter(default_state))
user_router.callback_query.register(send_edited_imagefile, F.data == 'send_file',
                                    StateFilter(FSMImageEditor.edit_image))
user_router.callback_query.register(end_editing_imagefile, F.data == 'end_edit', StateFilter(FSMImageEditor.edit_image))
user_router.callback_query.register(process_imagefile, F.data.in_(LEXICON_KB), StateFilter(FSMImageEditor.edit_image))
