from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

asosiy_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🖥Kurslar haqida",),
            KeyboardButton(text="📝Kursga yozilish"),
        ],
        [
            KeyboardButton(text="☎️ Aloqa va Manzil"),
        ]
    ],
    resize_keyboard=True
)

kurslar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Kompyuter savodxonligi"),
        ],
        [
            KeyboardButton("Frontend"),
            KeyboardButton("Backend"),
        ],
        [
            KeyboardButton("Grafik dizayn"),
            KeyboardButton("IT English"),
        ],
        [
            KeyboardButton("One Million Uzbek Coders")
        ],
        [
            KeyboardButton("🔙 Qaytish")
        ]
    ],
    resize_keyboard=True
)

yozilish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📝Kompyuter savodxonligi"),
        ],
        [
            KeyboardButton("📝Frontend"),
            KeyboardButton("📝Backend"),
        ],
        [
            KeyboardButton("📝Grafik dizayn"),
            KeyboardButton("📝IT English"),
        ],
        [
            KeyboardButton("📝One Million Uzbek Coders")
        ],
        [
            KeyboardButton("🔙 Qaytish")
        ]
    ],
    resize_keyboard=True
)

qaytish_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🔙 Qaytish")
        ]
    ],
    resize_keyboard=True
)
