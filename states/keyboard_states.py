from aiogram.dispatcher.filters.state import StatesGroup,State

class KeyboardState(StatesGroup):
    get_telefon=State()
    menu=State()
    kurslar=State()
    yozilish=State()