from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from keyboards.default.menu import asosiy_menu

@dp.message_handler(Command("Dasturchilar", prefixes="!/"))
async def bot_start(message: types.Message):
    await message.delete()
    await message.answer(f"Salom {message.from_user.full_name}\n Adminlar:\n \n```````````````````\n \n <a href='https://t.me/Mx_2589/'>Dasturchi</a>: Muhammadamin Ahmedov\n Va Fayzullo Asqarov\n \n```````````````````\n",disable_web_page_preview=True)

