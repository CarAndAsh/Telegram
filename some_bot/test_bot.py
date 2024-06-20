from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
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
    await msg.reply(f'Сам ты - {msg.text}')

disp.message.register(start_cmnd_answer, Command(commands=('start',)))
disp.message.register(help_cmnd_answer, Command(commands=('help',)))
disp.message.register(any_msg_answer)


if __name__ == '__main__':
    disp.run_polling(bot)
