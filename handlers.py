from main_telega import  bot, dp
from aiogram.types import Message
from configure import admin_id
async def sent_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Bot Started")

@dp.message_handler()
async  def echo(message: Message):
    text = f"Privet, ti napsial:{message.text}"
    await  bot.send_message(chat_id=message.from_user.id, text=text)
    await message.answer(text=text)