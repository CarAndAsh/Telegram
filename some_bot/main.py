from asyncio import run
from aiogram import Bot, Dispatcher

from config_data.config import load_config, Config
from handlers.user import user_router
from handlers.other import other_router
from middleware.inner import (FirstInnerMiddleware, SecondInnerMiddleware, ThirdInnerMiddleware)
from middleware.outer import (FirstOuterMiddleware, SecondOuterMiddleware, ThirdOuterMiddleware)
from log_config import logger


# TODO


async def main_func():
    config: Config = load_config('./.env')
    test_bot = Bot(config.tg_bot.token)
    dp = Dispatcher()
    desc = 'Приветствую тебя, пользователь!\n' \
           'Здесь может быти реализован различный функционал.' \
           '\nБуду держать тебя в курсе, что здесь можно делать и как.\n' \
           'В данный момент тестируем внутренности =)'
    name = 'Бот с миддлварями'
    short_desc = 'Данный бот предназначен для реализации заданий из курса https://stepik.org/course/120924'
    dp.include_router(user_router)
    dp.include_router(other_router)
    dp.update.outer_middleware(FirstOuterMiddleware())
    user_router.callback_query.middleware(FirstInnerMiddleware())
    other_router.callback_query.middleware(SecondInnerMiddleware())
    user_router.message.outer_middleware(SecondOuterMiddleware())
    other_router.message.outer_middleware(ThirdOuterMiddleware())
    user_router.message.middleware(ThirdInnerMiddleware())

    logger.info('Start bot')
    if await test_bot.get_my_description() != desc:
        await test_bot.set_my_description(description=desc)
    if await test_bot.get_my_short_description() != short_desc:
        await test_bot.set_my_short_description(short_description=short_desc)
    if await test_bot.get_my_name() != name:
        await test_bot.set_my_name(name=name)
    await test_bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(test_bot, polling_timeout=40)


run(main_func())
