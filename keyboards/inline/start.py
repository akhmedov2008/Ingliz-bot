from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from keyboards.callbacks.callback_datas import source_callback
source_callbacks = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kompyuter savodxonligi",callback_data=source_callback.new(kurs_nomi='kompyuter_savodxonligi')),
        ],
        [
            InlineKeyboardButton(text="FrontEnd dasturlash",callback_data=source_callback.new(kurs_nomi='frontend')),
        ],
        [
            InlineKeyboardButton(text="Mobil robototexnika",callback_data=source_callback.new(kurs_nomi='robototexnika')),
        ],
        [
            InlineKeyboardButton(text="Python backend",callback_data=source_callback.new(kurs_nomi='python-backend')),
        ],
        [
            InlineKeyboardButton(text="Veb dizayn",callback_data=source_callback.new(kurs_nomi='veb-dizyn')),
        ],
        [
            InlineKeyboardButton(text="Grafik dizayn",callback_data=source_callback.new(kurs_nomi='grafik-dizayn'))
        ],
        [
            InlineKeyboardButton(text="Kibersport",callback_data=source_callback.new(kurs_nomi="kibersport"))
        ],
        [
            InlineKeyboardButton(text="IT-English",callback_data=source_callback.new(kurs_nomi="it-english"))
        ]
    ],
    row_width=1,
)
