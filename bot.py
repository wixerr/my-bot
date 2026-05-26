import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import BOT_TOKEN, BANKS

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    builder = InlineKeyboardBuilder()
    for bank_name in BANKS:
        builder.button(text=bank_name, callback_data=f"bank_{bank_name}")
    builder.adjust(1)
    await message.answer(
        "Привет! Я помогу тебе оформить банковскую карту и получить выгоду.\n\n"
        "Выбери банк:",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(lambda c: c.data.startswith("bank_"))
async def bank_chosen(call: CallbackQuery):
    bank_name = call.data.replace("bank_", "")
    bank = BANKS[bank_name]
    await call.message.answer(
        f"Банк: {bank_name}\n"
        f"Вознаграждение: {bank['reward']}\n\n"
        f"Инструкция:\n{bank['instruction']}\n\n"
        f"Ссылка для оформления:\n{bank['link']}"
    )
    await call.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
