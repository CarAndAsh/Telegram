from aiogram import Bot
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot_core.bot import create_bot, name_and_desc_check_and_set, create_dispatcher
from bot_core.config import settings
from bot_core.log_cofig import logger

logger.name = __file__

LOCAL_BOT_HOST = '0.0.0.0'
LOCAL_BOT_PORT = 8080

WEBHOOK_PATH = '/bots/webhook'
WEBHOOK_SECRET = ''
WEBHOOK_BASE_URL = 'https://replit.com/@CarAndAsh/Telegram'


async def on_startup(bot: Bot) -> None:
    await name_and_desc_check_and_set(bot)
    me = await bot.get_me()
    logger.warning(f'Бот {me.username} запущен')
    wh_info =  await bot.get_webhook_info()
    wh_url = WEBHOOK_BASE_URL + WEBHOOK_PATH
    if wh_info.url != wh_url:
        await bot.delete_webhook(drop_pending_updates=False)
        await bot.set_webhook(
            url=wh_url,
            # secret_token=WEBHOOK_SECRET
        )
        logger.warning(f'Webhook установлен на {wh_url}')
        ###


def create_prepared_web_app() -> web.Application:
    bot = create_bot()
    dp = create_dispatcher()
    dp.startup.register(on_startup)

    web_app = web.Application()
    aiogram_webhook_req_handler = SimpleRequestHandler(
        dispatcher=dp, bot=bot, handle_in_background=False,
        # secret_token=WEBHOOK_SECRET
    )
    aiogram_webhook_req_handler.register(web_app, path=WEBHOOK_PATH)
    setup_application(web_app, dp, bot=bot)
    return web_app


def main() -> None:
    app = create_prepared_web_app()
    web.run_app(app, host=LOCAL_BOT_HOST, port=LOCAL_BOT_PORT)


if __name__ == '__main__':
    main()
