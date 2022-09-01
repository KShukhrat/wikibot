from aiogram import Bot, Dispatcher, executor, types
import wikipedia as w
import logging


logging.basicConfig(level=logging.INFO)

w.set_lang("uz")

TOKEN = 'TOKEN UCHUN'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Wikipeida Botiga Xush Kelibsiz!\nSiz hohlagan narsangizni qidiridirishingiz mumkin.\nQidirish uchun kerakli bo'lgan matnnit kiriting!!!")

@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.reply("Qidirilayotgan matnni kiriting!!!")

@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        await message.reply(w.summary(message.text))
    except:
        await message.reply("Siz izlayotgan narsa topilmadi😅")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
