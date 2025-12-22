__all__  = ('router',)

from aiogram import Router
from other import other_router

router = Router()
router.include_router(other_router)