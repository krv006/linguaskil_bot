from aiogram import Bot, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, FSInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_router = Router()

url = "https://docs.google.com/forms/d/e/1FAIpQLSdiShe6TGsuRri-IArB9PSLbS5JX_C1zU_Rs8zguFgcBb6HSQ/viewform?usp=pp_url"


@main_router.message(CommandStart())
async def start_handler(message: Message):
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text="Ro'yxatdan o'tish"), KeyboardButton(text="To'lov qilish"))
    rkb.adjust(2, repeat=True)
    await message.answer(text="Assalomu Alaykum, botimizga xush kelibsiz",
                        reply_markup=rkb.as_markup(resize_keyboard=True))


@main_router.message(F.text == "Ro'yxatdan o'tish")
async def royxatdan_handler(message: Message):
    await message.answer(url)
    await message.answer("Mana shu havola orqali ro'yxatdan o'tishingiz mumkin!")


@main_router.message(F.text == "To'lov qilish")
async def tolov_qilish_handler(message: Message, bot: Bot):
    image = FSInputFile('image_2024-06-13_09-05-59.png')
    await bot.send_photo(message.chat.id, image)
    await message.answer("Mana shu QR code ni skaner qilib oling va to'lo'vdi amalga ishiring !")
