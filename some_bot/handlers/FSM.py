from aiogram.fsm.state import StatesGroup, State


class FSMFormAboutUser(StatesGroup):
    choose_gender = State()
    fill_name = State()
    fill_second_name = State()
    fill_age = State()
    fill_education = State()
    upload_photo = State()
