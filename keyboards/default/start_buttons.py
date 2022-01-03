from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

get_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 raqamni yuborish",request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)