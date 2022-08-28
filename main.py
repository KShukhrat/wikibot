from aiogram import Bot, Dispatcher, executor, types
import wikipedia as w
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)

w.set_lang("ru")
# Configure bot
TOKEN = '5327095492:AAGbxmcWU4F48HnrTBkwmZODQ7abNvOiRiI'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("""Hello, I'm Wikipedia bot.
                        I can search for you wikipedia articles.
                        Just send me a word or phrase and I'll search for it.""")

@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.reply("Just send me a word or phrase and I'll search for it.")

@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        await message.reply(w.summary(message.text))
    except:
        await message.reply("I can't find anything for you :(")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)