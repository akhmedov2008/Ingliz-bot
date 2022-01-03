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
from keyboards.default.menu import asosiy_menu


@dp.message_handler(IsGroup(),CommandStart())
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer(f"Assalom aleykum {message.from_user.full_name}.\n @Paxtaobod_IT_Center Guruhiga Xush kelibsiz\n Kursga yozilish uchun pastdagi tugmani bosing\n 👇👇👇",
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Bot ga o'tish",url="@Paxtaobod_IT_Center_bot")]]),
                         disable_web_page_preview=True)
    await message.delete()


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

