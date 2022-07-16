from statistics import mean
import aiogram
from aiogram import Bot, Dispatcher, executor, types
import logging
import random
import surrogates

POSSIBLE_MESSAGES_1 = ["Я тебя люблю", "я тебя люблю", "люблю", "Люблю", "Люблю тебя", "люблю тебя", "Очень люблю", "очень люблю", "Очень тебя люблю", "очень тебя люблю", "лю", "Лю"]

STICKER_ID = [r"CAACAgIAAxkBAAEFS2Bi0uTl5VksbT7MFs2B1b7triuvTQACchUAAl6_6Eod1eqw4T11iykE", r"CAACAgIAAxkBAAEFS2Ji0uTqlfrBOICGn8E5xKoxvSQBiAACWAEAAhZCawr58l8Xq0rOmSkE", r"CAACAgIAAxkBAAEFS2Ri0uWUa1bp_OZJHOQb38NavPhs8AACnxUAAl1ZyEtEDa1wW6NsuSkE",
r"CAACAgIAAxkBAAEFS2xi0uXBLBPKxYtKjanIcoDfke8y0gACyxYAAnxm8EuP4x0kiBt81ykE", r"CAACAgIAAxkBAAEFS25i0uXjNqfIr1wKcrVe8tdH3oI7LAACyBUAAhkE6EggM6bGMMq_2ykE",
r"CAACAgEAAxkBAAEFS3Bi0uYLwPMX2byx6j35O-EKcTv9nwACxgEAAuN6wEZJbRJpFPQWKikE", 
r"CAACAgIAAxkBAAEFS3Ji0uYqLoE9-wAB9CbNe3eWarU-VzQAAnwRAAL2x6hLkbePhpbcIpYpBA"]

PHRASE_LIST_1 = ["Я тебя тоже", "А я своего котика сильнее лбюлю", "Люблю люблю люблю люблю люблю люблю люблю люблю люблю люблю люблю люблю люблю", "хехеххе, все равно я тебя сильнее люблю", "Я тебя тоже, котик", "лю", "Лю", "Я тебя так сильно люблю", "я тебя так сильно люблю"]

BOT_TOKEN = "your TOKEN"
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def get_started(message: types.Message):
    await message.answer("Привет, я бот созданный для любви! \nСо мной ты можешь: \n1)Признаться о том как ты сильно меня любишь)) \n2)Рассказать мне если у тебя что-то болит(((")
    

@dp.message_handler()
async def cath_message(message: types.Message):
    if (message.text in POSSIBLE_MESSAGES_1 or "люблю тебя" in message.text or "тебя люблю" in message.text) and message.from_id != your id:
        await message.answer(random.choice(PHRASE_LIST_1))
        await message.answer_sticker(random.choice(STICKER_ID))
    elif ("болит" in message.text or "Болит" in message.text or "Ударилась" in message.text or "ударилась" in message.text or "Больно" in message.text or "больно" in message.text or "Разбила" in message.text or "разбила" in message.text) and message.from_id != your id:
        await message.answer("Ууммм моему котику больно, дай поцелую!")
        await message.answer_sticker(r"CAACAgIAAxkBAAEFS15i0uC5hiP0yFSQCUE1qkqzy-lo4gACnxUAAl1ZyEtEDa1wW6NsuSkE") 
    elif message.from_id != your id:
        await message.answer("Извини, любимая, я не рассчитал, что ты можешь так сказать. Люблю тебя!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
