from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import json

with open('tokens.json') as f:
    j = json.load(f)
    BOT_TOKEN = j['test_zeixes_bot token']

bot = Bot(BOT_TOKEN)
disp = Dispatcher()


async def start_cmnd_answer(msg: Message):
    await msg.answer('Рад приветствовать Вас в нашей таверне =)')


async def help_cmnd_answer(msg: Message):
    await msg.answer('Чем я могу Вам помочь?')


async def any_msg_answer(msg: Message):
    print(msg.sticker)
    await msg.reply(f'Сам(-а) ты - {msg.text}')


async def photo_msg_answer(msg: Message):
    await msg.reply_photo(msg.photo[0].file_id)


async def sticker_answer(msg: Message):
    await msg.reply_sticker(sticker=msg.sticker.file_id)


async def GIF_answer(msg: Message):
    await msg.reply_sticker(sticker=msg.animation.file_id)


disp.message.register(start_cmnd_answer, Command(commands=('start',)))
disp.message.register(help_cmnd_answer, Command(commands=('help',)))
# this for example, after use F.<content_type>
disp.message.register(photo_msg_answer, F.content_type == ContentType.PHOTO)
disp.message.register(sticker_answer, F.sticker)
disp.message.register(GIF_answer, F.animation)
disp.message.register(any_msg_answer)

if __name__ == '__main__':
    disp.run_polling(bot)
