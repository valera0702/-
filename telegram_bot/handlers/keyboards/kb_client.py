from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 



katalog = KeyboardButton("Каталог")
local = KeyboardButton("Расположение")
assist = KeyboardButton("Помощь")
contact = KeyboardButton("Поделиться контактом", request_contact=True)
where_i = KeyboardButton("Отправить где я",request_location=True)
client_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(katalog).row(local, assist).row(contact, where_i)
