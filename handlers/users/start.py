from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.reply(f"👋 <b>Assalomu alaykum {message.from_user.first_name}</b>"
                        f"\n\n✅❌ Bu bot siz kiritgan so'z yoki so'zlarni imloviy xato yoki to'g'riligini tekshirib beradi"
                        f"\n\n<i>Botdan foydalanish uchun iltimos tekshirmoqchi bo'lgan so'z yoki so'zlaringizni yuboring...</i>")
