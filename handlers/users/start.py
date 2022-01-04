from aiogram import types
from aiogram.types import ContentType,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from states.keyboard_states import KeyboardState
from loader import dp
from filters.group_filters import IsGroup
from keyboards.default.start_buttons import get_number
from states.keyboard_states import KeyboardState
import asyncio
from filters.private_chat import IsPrivate
from keyboards.default.menu import asosiy_menu

@dp.message_handler(CommandStart(),IsGroup())
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer(f"Assalom aleykum {message.from_user.full_name}.\n @Paxtaobod_IT_Center Guruhiga Xush kelibsiz\n Kursga yozilish uchun <a href='https://t.me/Paxtaobod_it_center_bot'>BOT</a> ga o'ting\n ",
                         disable_web_page_preview=True)
    await message.delete()
    await asyncio.sleep(0.5)



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer(text="🔑 Assalomu alaykum!\n📑 Botdan foydalanish uchun iltimos quyidagi tugma orqali raqamingizni yuboring!",reply_markup=get_number)
    await state.set_state(KeyboardState.get_telefon)

@dp.message_handler(CommandStart(),state=KeyboardState.menu)
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer(text="🔑 Assalomu alaykum!\n📑 Botdan foydalanish uchun iltimos quyidagi tugma orqali raqamingizni yuboring!",reply_markup=get_number)
    await state.set_state(KeyboardState.get_telefon)
@dp.message_handler(CommandStart(),state=KeyboardState.kurslar)
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer(text="🔑 Assalomu alaykum!\n📑 Botdan foydalanish uchun iltimos quyidagi tugma orqali raqamingizni yuboring!",reply_markup=get_number)
    await state.set_state(KeyboardState.get_telefon)

@dp.message_handler(CommandStart(),state=KeyboardState.get_telefon)
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer(text="🔑 Assalomu alaykum!\n📑 Botdan foydalanish uchun iltimos quyidagi tugma orqali raqamingizni yuboring!",reply_markup=get_number)
    await state.set_state(KeyboardState.get_telefon)


