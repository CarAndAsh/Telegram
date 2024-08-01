from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Dict, Any, Callable, Awaitable
from log_config import logger


class FirstOuterMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        logger.debug(f'Enter middleware {__class__.__name__} when {event.__class__.__name__}')
        result = await handler(event, data)
        logger.debug(f'Exit middleware {__class__.__name__} when {event.__class__.__name__}')
        return result


class SecondOuterMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        logger.debug(f'Enter middleware {__class__.__name__} when {event.__class__.__name__}')
        result = await handler(event, data)
        logger.debug(f'Exit middleware {__class__.__name__} when {event.__class__.__name__}')
        return result


class ThirdOuterMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        logger.debug(f'Enter middleware {__class__.__name__} when {event.__class__.__name__}')
        result = await handler(event, data)
        logger.debug(f'Exit middleware {__class__.__name__} when {event.__class__.__name__}')
        return result
