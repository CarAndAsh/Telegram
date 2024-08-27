from aiogram.fsm.state import StatesGroup, State


class FSMImageEditor(StatesGroup):
    edit_image = State()
