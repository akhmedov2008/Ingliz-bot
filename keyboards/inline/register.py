from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard



tasdiqlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Tasdiqlash",callback_data="yozilish_tsdiqlash"),
            InlineKeyboardButton(text="❌Bekor qilish",callback_data="yozilish_bekorqilish"),
        ],
    ],
    row_width=2,
)