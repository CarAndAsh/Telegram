from random import choice
from lexicon.lexicon_ru import LEXICON_KB_RU

RULES = {'rock': ('scissors', 'lizard'),
         'scissors': ('paper', 'lizard'),
         'paper': ('rock', 'spock'),
         'lizard': ('paper', 'spock'),
         'spock': ('scissors', 'rock')}


def get_bot_choice():
    return choice(('rock', 'paper', 'scissors', 'lizard', 'spock'))


def _normalize_user_chioce(user_choice):
    for key in LEXICON_KB_RU:
        if LEXICON_KB_RU[key] == user_choice:
            return key


def get_winner(user_choice: str, bot_choice: str):
    user_choice = _normalize_user_chioce(user_choice)
    if user_choice == bot_choice:
        return 'nobody'
    elif bot_choice in RULES[user_choice]:
        return 'won'
    return 'lose'
