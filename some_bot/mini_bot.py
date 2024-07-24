from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import (InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton)

from environs import Env

env = Env()
env.read_env('.env')
token = env('TOKEN')
bot = Bot(token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

callback_prefix = 'btn'
callback_sep = '-'

class BtnCallbackFactory(CallbackData, prefix=callback_prefix, sep=callback_sep):
    with_builder: int
    btn_id: int


btn_1 = InlineKeyboardButton(text='КНОПКА 1', callback_data=BtnCallbackFactory(
    with_builder=0,
    btn_id=1).pack())
btn_2 = InlineKeyboardButton(text='КНОПКА 2', callback_data=BtnCallbackFactory(
    with_builder=0,
    btn_id=2).pack())

keyboard_1 = InlineKeyboardMarkup(inline_keyboard=[[btn_1], [btn_2]])
kb_builder = InlineKeyboardBuilder()
kb_builder.row(*[InlineKeyboardButton(
    text=f'КНОПКА {btn_id}',
    callback_data=BtnCallbackFactory(with_builder=1, btn_id=btn_id).pack()) for btn_id in range(1, 4)]
               )
kb_builder.adjust(1,2)


@dp.message(CommandStart())
async def work_on_start(msg: Message):
    await msg.answer('Привет, вот тебе клава, поиграйся', reply_markup=keyboard_1)


@dp.callback_query()
async def work_on_callback(callback: CallbackQuery):
    if callback.data.startswith(f'{callback_prefix}{callback_sep}0'):
        await callback.message.edit_text(f'Была нажата кнопка {callback.data}', reply_markup=(kb_builder.as_markup()))
    else:
        await callback.message.edit_text(f'Была нажата кнопка {callback.data}', reply_markup=keyboard_1)


bot.delete_webhook(drop_pending_updates=True)
dp.run_polling(bot)
