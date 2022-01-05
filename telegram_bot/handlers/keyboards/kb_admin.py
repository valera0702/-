from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 



load = KeyboardButton("Загрузить")
back = KeyboardButton("Отмена")
delet = KeyboardButton("Удалить")
admin_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(load, back).row(delet)
