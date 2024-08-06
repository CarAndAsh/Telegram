from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon_ru import LEXICON_MENU_RU


async def set_menu(bot: Bot):
    main_menu_cmnds = [BotCommand(command=cmnd, description=LEXICON_MENU_RU[cmnd]) for cmnd in LEXICON_MENU_RU]
    await bot.set_my_commands(main_menu_cmnds)
