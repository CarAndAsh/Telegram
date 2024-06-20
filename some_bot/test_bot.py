from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import json

with open('tokens.json') as f:
    j = json.load(f)
    BOT_TOKEN = j['test_zeixes_bot token']

bot = Bot(BOT_TOKEN)
disp = Dispatcher()


@disp.message(Command(commands=('start',)))
async def start_cmnd_answer(msg: Message):
    await msg.answer('Рад приветствовать Вас в нашей таверне =)')


@disp.message(Command(commands=('help',)))
async def help_cmnd_answer(msg: Message):
    await msg.answer('Чем я могу Вам помочь?')


@disp.message()
async def any_msg_answer(msg: Message):
    await msg.reply(f'Сам ты - {msg.text}')

if __name__ == '__main__':
    disp.run_polling(bot)
