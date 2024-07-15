from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon_ru import LEXICON_MENU_RU


async def set_menu(bot: Bot):
    main_menu = [BotCommand(command=cmnd, description=dsc) for cmnd, dsc in LEXICON_MENU_RU.items()]
    await bot.set_my_commands(main_menu)
