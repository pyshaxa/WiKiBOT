import logging
import wikipedia
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '7930145827:AAFwAbvfN7iD0dApXXkeRpbLvh-STrqk8ss'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("SALOM!\nWiKiBOTga xush kelibsiz!\nMeni Shaxriyor yaratdi.")

@dp.message()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summery(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
