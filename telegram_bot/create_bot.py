from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot("5053891935:AAF4L55c1uQwyoZZlZgZuMpyFzlEQcOsuMY")
dp = Dispatcher(bot, storage=storage)