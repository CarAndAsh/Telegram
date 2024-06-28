from random import randint

from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message
import json

# TODO
# TODO
# TODO

with open('tokens.json') as f:
    j = json.load(f)
    BOT_TOKEN = j['test_zeixes_bot token']

bot = Bot(BOT_TOKEN)
disp = Dispatcher()


class NumbersInMessage(BaseFilter):
    async def __call__(self, msg: Message) -> bool | dict[int]:
        nums = list(filter(lambda word: word.isnumeric(),
                           [word.replace('.', ' ').replace(',', ' ').strip() for word in msg.text.split()]))
        return {'numbers': nums} if nums else False


async def process_if_numbers(msg: Message, numbers: list[int]):
    await msg.answer(f'{", ".join(numbers)}')


async def process_if_not_numbers(msg: Message):
    await msg.answer('Нет чисел в данном тексте')


disp.message.register(process_if_numbers, F.text.lower().startswith('найди числа'), NumbersInMessage())
disp.message.register(process_if_not_numbers, F.text.lower().startswith('найди числа'))

if __name__ == '__main__':
    disp.run_polling(bot)
