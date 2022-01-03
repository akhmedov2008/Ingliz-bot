from aiogram import types
from filters.group_filters import IsGroup
from loader import dp


# Echo bot
@dp.message_handler(IsGroup(),state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
