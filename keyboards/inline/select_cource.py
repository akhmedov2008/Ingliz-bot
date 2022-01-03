from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.callbacks.callback_datas import kursga_yozilish
def build_keyboard(cource_name):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Kursga yozilish",callback_data=kursga_yozilish.new(yozilish="ha",kurs_nomi=cource_name)),
                InlineKeyboardButton(text="Ko'proq malumot",callback_data=kursga_yozilish.new(yozilish="koproq",kurs_nomi=cource_name))
            ]
        ],
        row_width=1
    )

# InlineKeyboardMarkup([[InlineKeyboardButton("Kursga yozilish",callback_data='kompyuter_savodhonligiga_yozildi'),InlineKeyboardButton("Ko'proq malumot",callback_data='koproq_comp')]]))