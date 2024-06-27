from random import randint

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ContentType
import json

# TODO buttons
# TODO DB
# TODO multiplayer

with open('tokens.json') as f:
    j = json.load(f)
    BOT_TOKEN = j['test_zeixes_bot token']

bot = Bot(BOT_TOKEN)
disp = Dispatcher()

users = {}

user = {}
ATTEMPTS = 5


async def start_cmnd_answer(msg: Message):
    await msg.answer('Рад приветствовать Вас в нашей таверне =)'
                     '\nСыграем в "Угадай число"?\nИнформация по игре - /help.')
    user_id = msg.from_user.id
    if user_id not in users:
        users[user_id] = {'in_game': False, 'secret_number': None, 'attempts': None, 'total_games': 0, 'wins': 0}


async def help_cmnd_answer(msg: Message):
    await msg.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                     f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                     f'попыток\n\nДоступные команды:\n/help - правила '
                     f'игры и список команд\n/cancel - выйти из игры\n'
                     f'/stat - посмотреть статистику\n\nДавай сыграем?')


async def ask_stat(msg: Message):
    await msg.answer(
        f'Всего игр сыграно: {users[msg.from_user.id]["total_games"]} \nПобед: {users[msg.from_user.id]["wins"]}')


async def user_agreed(msg: Message):
    if not users[msg.from_user.id]['in_game']:
        users[msg.from_user.id]['in_game'] = True
        users[msg.from_user.id]['secret_number'] = randint(1, 100)
        users[msg.from_user.id]['attempts'] = ATTEMPTS
        await msg.answer('Я загадал число, попробуй угадай')


async def user_disagreed(msg: Message):
    if users[msg.from_user.id]['in_game']:
        await msg.answer('Если мы уже играем, то для выхода используй /cancel')
    else:
        await msg.answer('Жаль, но если что пиши...')


async def number_answer(msg: Message):
    if users[msg.from_user.id]['in_game']:
        if (try_num := int(msg.text)) == users[msg.from_user.id]['secret_number']:
            users[msg.from_user.id]['total_games'] += 1
            users[msg.from_user.id]['wins'] += 1
            users[msg.from_user.id]['in_game'] = False
            await msg.answer('Угадал!!!\nМожет еще разок?')
        else:
            await msg.answer(
                'Твое число ' + ('меньше' if (try_num < users[msg.from_user.id]['secret_number']) else 'больше'))
            users[msg.from_user.id]['attempts'] -= 1
        if users[msg.from_user.id]['attempts'] == 0:
            users[msg.from_user.id]['in_game'] = False
            users[msg.from_user.id]['total_games'] += 1
            await msg.answer(f'К сожалению, у вас больше не осталось '
                             f'попыток. Вы проиграли :(\n\nМое число '
                             f'было {users[msg.from_user.id]["secret_number"]}\n\nДавайте '
                             f'сыграем еще?')
    else:
        await msg.answer('Мы даже еще и не начинали')


async def user_canceled(msg: Message):
    if users[msg.from_user.id]['in_game']:
        await msg.answer('Если мы уже играем, то для выхода используй /cancel')
    else:
        await msg.answer('Подожди, мы еще не начали')


async def any_msg_answer(msg: Message):
    if users[msg.from_user.id]['in_game']:
        await msg.answer('Мы уже играем, пришли мне число от 1 до 100')
    else:
        await msg.answer('Такие команды я не понимаю, лучше давай сыграем')


disp.message.register(start_cmnd_answer, CommandStart())
disp.message.register(help_cmnd_answer, Command(commands=('help',)))
disp.message.register(user_agreed, F.text.lower().in_(['да', 'ок', 'согласен', 'давай', 'запускай']))
disp.message.register(user_disagreed, F.text.lower().in_(['нет', 'не хочу', 'не согласен', 'не буду', 'отстань']))
disp.message.register(number_answer, lambda answ: answ.text and answ.text.isnumeric() and 1 <= int(answ.text) <= 100)
disp.message.register(user_canceled, Command(commands=('cancel',)))
disp.message.register(ask_stat, Command(commands=('stat',)))
disp.message.register(any_msg_answer)

if __name__ == '__main__':
    disp.run_polling(bot)
