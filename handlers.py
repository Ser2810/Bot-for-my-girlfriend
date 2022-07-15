import asyncio
from aiogram import types
from main import dp 

@dp.message_handler(commands="start")
async def start(message: types.Message):
   await message.reply("Привет! \nНапиши мне что угодно!")

async def echo(message: types.Message):
   await message.reply(f"Ты написал: {message.text}")
