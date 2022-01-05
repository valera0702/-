from aiogram import types, Dispatcher
from create_bot import dp, bot
from handlers.keyboards.kb_client import client_kb


def reg_client(dp: Dispatcher):
  dp.register_message_handler(katalog, lambda message:"Каталог" in message.text)
  dp.register_message_handler(local,  lambda message:"Расположение" in message.text)
  dp.register_message_handler(assist, lambda message:"Помощь" in message.text)
  dp.register_message_handler(start, commands=['start'])


async def katalog(message: types.Message):
    await bot.send_message(message.from_user.id, "Пусто")

async def local(message: types.Message):
    await bot.send_message(message.from_user.id, "улица Бжегокайская 31/4 к2")

async def assist(message: types.Message):
    await bot.send_message(message.from_user.id, "в лс @yourickrolled")

async def start(message: types.Message):
  await bot.send_message(message.from_user.id, "Приятных покупок{}" .format(message.from_user.first_name), reply_markup=client_kb) 

