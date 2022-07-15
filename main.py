from aiogram import Bot, Dispatcher, executor, types
import logging


BOT_TOKEN = "5521938306:AAF2jC6KuvCYOS-BUMx15Uq5TC53-rVZRsk"
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    await message.reply("Привет, я готов работать")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


