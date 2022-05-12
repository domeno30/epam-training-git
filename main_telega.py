import asyncio
from aiogram import Bot, Dispatcher, executor

import configure
from configure import BOT_TOKEN
import telebot
from telebot import types

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
if __name__ == "__main__":
    from handlers import dp, sent_to_admin

    executor.start_polling(dp, on_startup=sent_to_admin)
