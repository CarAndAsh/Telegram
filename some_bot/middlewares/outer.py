from re import match
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.fsm.state import default_state
from aiogram.types import TelegramObject

from handlers.FSM import FSMFormAboutUser
from lexicon.lexicon_ru import LEXICON_KB_RU
from log_config import logger


class FSMMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:

        match await data['state'].get_state(), event.text:
            case default_state, '/fill_form':
                logger.info(f'FSM Middleware ')
                return await handler(event, data)
            case FSMFormAboutUser.choose_gender, text if text in LEXICON_KB_RU['gender'].values():
                logger.info(f'FSM Middleware 1')
                return await handler(event, data)
            case FSMFormAboutUser.fill_name, text if match('[A-Z][a-z]+?', text):
                logger.info(f'FSM Middleware 2')
                return await handler(event, data)
            case FSMFormAboutUser.fill_second_name, text if match('[A-Z][a-z]+?', text):
                logger.info(f'FSM Middleware 3')
                return await handler(event, data)
            case FSMFormAboutUser.fill_age, text if match('[0-9]+?', text):
                logger.info(f'FSM Middleware 4')
                return await handler(event, data)
            case FSMFormAboutUser.fill_education, text if text in LEXICON_KB_RU['edu'].values():
                logger.info(f'FSM Middleware 5')
                return await handler(event, data)
            case FSMFormAboutUser.upload_photo:
                logger.info(f'FSM Middleware 6')
                return await handler(event, data)
            case _, cmnd if cmnd in ('/cancel', '/start', '/help'):
                logger.info(f'FSM Middleware 7')
                return await handler(event, data)
            case _, _:
                logger.info(f'FSM Middleware missing')
