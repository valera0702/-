import logging
from aiogram import executor
from create_bot import dp
from data_base import sqlite_db

async def on_startup(_):
    print("бот вышел в онлайн")
    sqlite_db.start()


from handlers import client, admin

client.reg_client(dp)
admin.reg_admin(dp)


if __name__ == "__main__":
 executor.start_polling(dp, skip_updates = True, on_startup=on_startup)