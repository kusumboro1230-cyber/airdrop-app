import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Yahan apna bilkul naya wala token paste karo (quotes ke andar)
BOT_TOKEN = "9189384737:AAFHUpzdlbMiGfaINM651pmi4j5U8mBBiAg"

WEB_APP_URL = "https://kusumboro1230-cyber.github.io/airdrop-app/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Open Game Analyzer App",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )
    
    await message.answer(
        "Welcome! Niche diye gaye button par click karke Web App open karein:",
        reply_markup=keyboard
    )

async def main():
    print("Bot is running successfully...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
