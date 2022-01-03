from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.default.menu import asosiy_menu
from keyboards.inline.register import tasdiqlash
from states.keyboard_states import KeyboardState
from loader import dp,bot
from data.config import ADMINS
from data.textlar_dict import kurslar_yozilish_javoblari

@dp.callback_query_handler(text="yozilish_tsdiqlash",state=[i.replace(' ','_') for i in kurslar_yozilish_javoblari.keys()])
async def tasdiqladi(call:CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.answer()
    result_text="✅ Arizangiz muvaffaqqiyatli yuborildi!\n🕓 Tez orada operator siz bilan bog'lanadi!\n\n🔹 Siz o'z safimizda ko'rishdan hursandmiz, Keling, Kelajakni birga quramiz!"
    await call.message.answer(result_text,reply_markup=asosiy_menu)
    await state.set_state(KeyboardState.menu)
    await bot.send_message(ADMINS[0],text=f"{kurslar_yozilish_javoblari[str(call.message.chat['id'])]}")
    kurslar_yozilish_javoblari.pop(str(call.message.chat.id))
@dp.callback_query_handler(text="yozilish_bekorqilish",state=[i.replace(' ','_') for i in kurslar_yozilish_javoblari.keys()])
async def delete_tasdiqlash(call:CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer("Bekor qilindi asosiy menudasiz",reply_markup=asosiy_menu)
    await state.set_state(KeyboardState.menu)



