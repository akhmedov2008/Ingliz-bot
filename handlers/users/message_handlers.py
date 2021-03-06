from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.group_filters import IsGroup
from loader import dp,bot
from keyboards.default.menu import kurslar_menu,asosiy_menu,yozilish,qaytish_button
from keyboards.inline.register import tasdiqlash
from data.textlar_dict import kurslar_yozilish_javoblari
from states.keyboard_states import KeyboardState
from keyboards.default.start_buttons import get_number
import asyncio
from time import sleep
@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def salomlash(message:types.Message):
    await message.delete()
    # text=f"Guruxga yangi azo {message.from_user.full_name} qo'shildi"
    tbp=""
    typing_symbol = "ā³"
    # await message.answer(".")
    messageid=message.message_id+1
    
    await message.answer(f"Guruxga yangi azo {message.from_user.full_name} qo'shildi",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Bot ga o'tish",url="https://t.me//Paxtaobod_IT_Center_bot")]]))
    await asyncio.sleep(0.05)

@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} guruhni tark etdi")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} guruhdan haydaldi "
                             f"Admin: {message.from_user.get_mention(as_html=True)}.")

@dp.message_handler(CommandStart(),state=[i.replace(' ','_') for i in kurslar_yozilish_javoblari.keys()])
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer(text="š Assalomu alaykum!\nš Botdan foydalanish uchun iltimos quyidagi tugma orqali raqamingizni yuboring!",reply_markup=get_number)
    await state.set_state(KeyboardState.get_telefon)


@dp.message_handler(text="āļø Aloqa va Manzil",state=KeyboardState.menu)
async def aloqa(message:types.Message):
    await message.answer("š¢ Paxtaobod tuman IT Center\nš Ish vaqti: 9:00 dan 18:00 gacha\nš Manzil: Paxtaobod tumani, Paxtaobod shahar, Amir Temur ko'chasi, 2 uy\nšØāš» Mas'ul xodim: Erkinboyev Muxtoriddin.\nāļø Telefon: +998934419888\nš Lokatsiya:\nhttps://goo.gl/maps/6Jrtn6koijFxnYEp9")

@dp.message_handler(content_types=ContentType.CONTACT,is_sender_contact=True,state=KeyboardState.get_telefon)
async def group_start(message:types.Message,state:FSMContext):
    await message.answer("š Raqamingiz tasdiqlandi, tashakkur!")
    await state.update_data(
        {'telefon':message.contact.phone_number}
    )
    await message.answer("š Assalomu alaykum!\nš¢ Raqamli texnologiyalar o\'quv markazi Andijon viloyati Paxtaobod tumani filiali botiga hush kelibsiz!\nšØāš» Bu yerda kurslarimiz haqida ma\'lumot olishingiz va kurslarimizga yozilishingiz mumkin.\nSiz endi asosiy menyudan foydalanishingiz mumkin",reply_markup=asosiy_menu)
    await KeyboardState.next()

@dp.message_handler(content_types=[ContentType.CONTACT,ContentType.TEXT],state=KeyboardState.get_telefon)
async def boshqa_contact(message:types.Message):
    await message.answer("Iltimos o'z raqamingizni yuboring")

# @dp.message_handler(content_types=,state=KeyboardState.get_telefon)
# async def boshqa_contact(message:types.Message):
#     await message.answer("Iltimos tugma orqali yuboring")


@dp.message_handler(text="š„Kurslar haqida",state=KeyboardState.menu)
async def kurslar_haqida(message:types.Message,state:FSMContext):
    await message.answer("š Bizda 7 ta O'quv kursi bor:\n1ļøā£ Kompyuter savodxonligi;\n2ļøā£ Frontend;\n3ļøā£ Backend;\n4ļøā£ Grafik dizayn;\n5ļøā£ IT English.\n6ļøā£ One Million Uzbek Coders.;\nš Qo'shimcha ma'lumot quyidagi menyuda:",reply_markup=kurslar_menu)
    await KeyboardState.next()
@dp.message_handler(text="Kompyuter savodxonligi",state=KeyboardState.kurslar)
async def kompyuter_savodhonligi(message:types.Message):
    await message.answer("Kompyuter savodxonligi.\n\nš Kompyuter bilan umumiy tanishuv, Ofis dasturlari (Word, Excel), internet bilan ishlash kabi bilimlar o'rgatiladi.\n\nš Kurs davomiyligi: 1 oy,\nš 1 haftada 3 kun dars,\nš 1 kunda 1 soat.\n\nš° Kurs narxi: 100 ming so'm,\nš³ To'lov usuli: PayMe/Bank.")

@dp.message_handler(text="Frontend",state=KeyboardState.kurslar)
async def kompyuter_savodhonligi(message:types.Message):
    await message.answer("š Frontend kursi.\n\nš Frontend (HTML, CSS, JavaScript), React JS, Bootstrap kabi bilimlar o'rgatiladi.\n\nš Kurs davomiyligi: 3 oy,\nš 1 haftada 3 kun dars,\nš 1 kunda 2 soat.\n\nš° Kurs narxi: 220 ming so'm/oyiga,\nš³ To'lov usuli: PayMe/Bank.")


@dp.message_handler(text="Backend",state=KeyboardState.kurslar)
async def kompyuter_savodhonligi(message:types.Message):
    await message.answer("š Backend kursi.\n\nš Backend kursida PHP, Python, NodeJS kabi bilimlar o'rgatiladi.\n\nš Kurs davomiyligi: 3 oy dan 9 oygacha,\nš 1 haftada 3 kun dars,\nš 1 kunda 2 soat.\n\nš° Kurs narxi: 320 ming so'm/oyiga,\nš³ To'lov usuli: PayMe/Bank.")



@dp.message_handler(text="Grafik dizayn",state=KeyboardState.kurslar)
async def kompyuter_savodhonligi(message:types.Message):
    await message.answer("š¼ Grafik dizayn kursi.\n\nš Grafik dizayn kursida Adobe illustrator, Photoshop, Sketching, Adobe InDesign kabi bilimlar o'rgatiladi.\\nnš Kurs davomiyligi: 3 oy dan 9 oygacha,\nš 1 haftada 3 kun dars,\nš 1 kunda 2 soat.\n\nš° Kurs narxi: 220 ming so'm/oyiga,\nš³ To'lov usuli: PayMe/Bank.")


@dp.message_handler(text="IT English",state=KeyboardState.kurslar)
async def kompyuter_savodhonligi(message:types.Message):
    await message.answer("š¬š§ IT English.\n\nš IT English kirish, IT sohasida Ingliz tili o'rni, IT sohasida ingliz tilidan foydalanish va natijaga erishish, xalqaro materiallar bilan ishlash, (Speaking va Grammar chuqurlashtirilgan holda) kabi bilimlar o'rgatiladi.\n\nš Kurs davomiyligi: 3 oy,\nš 1 haftada 3 kun dars,\nš 1 kunda 2 soat.\n\nš° Kurs narxi: 200 ming so'm/oyiga,\nš³ To'lov usuli: PayMe/Bank.")


@dp.message_handler(text="One Million Uzbek Coders",state=KeyboardState.kurslar)
async def kompyuter_savodhonligi(message:types.Message):
    await message.answer("šŗšæ One Million Uzbek Coders.\n\nš One Million Uzbek Coders loyihasi bilan tanishuv, ro'yhatdan o'tish, mustaqil ta'lim olish kabi bilimlar o'rgatiladi.\n\nš Jami 12 ta dars,\nš Kurs davomiyligi: 1 oy.\n\nš° Kurs narxi: Bepul")

@dp.message_handler(text="Raqamlashtirish va IT tadbirkorlik",state=KeyboardState.kurslar)
async def kompyuter_savodhonligi(message:types.Message):
    await message.answer("š Raqamlashtirish va IT tadbirkorlik asoslari.\n\nš Dasturlashni mustaqil ravishda oārganish darsi - 1 ta dars, Ingliz tilini mustaqil ravishda oārganish - 1 ta dars, Kompyuterda ishlash asoslari (Operatsion tizim, MS Office) - 1 ta dars, Internetda ishlash asoslari (pochta, brauzer) - 1 ta dars, āOne Million Uzbek Codersā loyihasi bilan tanishish - 1 ta dars, Bulutli texnologiya va servislarni ishda qoāllash (Google Drive, Sheets, Forms, Trello board) - 2 ta dars, Kompaniyani yuridik tashkil etish, internetda ish izlash, frilans - 2 ta dars, Loyiha va jamoani boshqarish, loyiha risklari va bahosi - 1 ta dars.\n\nš Jami 10 ta dars,\nš Kurs davomiyligi: 1 oy.\n\nš° Kurs narxi: Bepul")

@dp.message_handler(text="š Qaytish",state=KeyboardState.kurslar)
async def qaytish(message:types.Message,state:FSMContext):
    await message.answer("š¢ Raqamli texnologiyalar o\'quv markazi Andijon viloyati Paxtaobod tumani filiali botiga hush kelibsiz!\nšØāš» Bu yerda kurslarimiz haqida ma\'lumot olishingiz va kurslarimizga yozilishingiz mumkin.\nSiz endi asosiy menyudan foydalanishingiz mumkin",reply_markup=asosiy_menu)
    await state.set_state(KeyboardState.menu)


@dp.message_handler(text="šKursga yozilish",state=KeyboardState.menu)
async def kurslar_yozilish(message:types.Message,state:FSMContext):
    await message.answer(text="š¢ Raqamli texnologiyalar o\'quv markazi Andijon viloyati Paxtaobod tumani filiali botiga hush kelibsiz!\nšØāš» Bu yerda kurslarimiz haqida ma\'lumot olishingiz va kurslarimizga yozilishingiz mumkin.\nSiz endi asosiy menyudan foydalanishingiz mumkin",reply_markup=yozilish)
    await state.set_state(KeyboardState.yozilish)

@dp.message_handler(text="š Qaytish",state=KeyboardState.yozilish)
async def qaytish(message:types.Message,state:FSMContext):
    await message.answer("š¢ Raqamli texnologiyalar o\'quv markazi Andijon viloyati Paxtaobod tumani filiali botiga hush kelibsiz!\nšØāš» Bu yerda kurslarimiz haqida ma\'lumot olishingiz va kurslarimizga yozilishingiz mumkin.\nSiz endi asosiy menyudan foydalanishingiz mumkin",reply_markup=asosiy_menu)
    await state.set_state(KeyboardState.menu)


@dp.message_handler(text="š Qaytish",state=[i.replace(' ','_') for i in kurslar_yozilish_javoblari.keys()])
async def qaytish(message:types.Message,state:FSMContext):
    await message.answer("š¢ Raqamli texnologiyalar o\'quv markazi Andijon viloyati Paxtaobod tumani filiali botiga hush kelibsiz!\nšØāš» Bu yerda kurslarimiz haqida ma\'lumot olishingiz va kurslarimizga yozilishingiz mumkin.\nSiz endi asosiy menyudan foydalanishingiz mumkin",reply_markup=asosiy_menu)
    await state.set_state(KeyboardState.menu)




@dp.message_handler(content_types=ContentType.TEXT,state=KeyboardState.yozilish)
async def kurslar_yozilish(message:types.Message,state:FSMContext):
    try:
        await message.answer(text=f"{kurslar_yozilish_javoblari[message.text]}",reply_markup=qaytish_button)
        await state.set_state(message.text.replace(' ','_'))
        await state.update_data(
            {'yonalish':message.text}
        )
    except:
        await message.answer("Kurslar nomini quyidagi menyudan tanlashingiz mumkin")


@dp.message_handler(content_types=ContentType.TEXT,state=[i.replace(' ','_') for i in kurslar_yozilish_javoblari.keys()])
async def get_names(message:types.Message,state:FSMContext):
    data=await state.get_data()
    userdata=f"User:{message.from_user.get_mention()}\nIsm Familiya:{message.text}\nTanlagan kursingiz:{data.get('yonalish')}\ntelefon raqamingiz:{data.get('telefon')}\nMa'lumotlar to'g'ri bo'lsa operatorga yuborish uchun Tasdiqlashni bosing"
    await message.answer(userdata,reply_markup=tasdiqlash)
    kurslar_yozilish_javoblari[str(message.from_user.id)] = userdata
