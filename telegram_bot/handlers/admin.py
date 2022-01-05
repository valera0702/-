from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot
from data_base import sqlite_db
from handlers.keyboards.kb_admin import admin_kb

ID = None
class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()

async def start(message: types.Message):
	if message.from_user.id == ID:
		await FSMAdmin.photo.set()
		await message.reply("Загрузи фото")

async def cancel(message: types.Message, state: FSMContext):
	current_state = await state.get_state()
	if current_state is None:
		return
	await state.finish()
	await message.reply("Ок")

async def photo(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data["photo"] = message.photo[0].file_id
		await FSMAdmin.next()
		await message.reply("Teперь введи название")

async def name(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data["name"] = message.text
		await FSMAdmin.next()
		await message.reply("Введи описание")

async def desc(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data["description"] = message.text
		await FSMAdmin.next()
		await message.reply("Теперь укажи цену")

async def price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data["price"] = float(message.text)

		await sqlite_db.sql_add_cmd(state)
		await state.finish()
		await message.reply("ок")

async def make_changes(message: types.Message):
	global ID 
	ID = message.from_user.id 
	await bot.send_message(message.from_user.id, "Что надо, хозяин?", reply_markup=admin_kb)
	await message.delete()


def reg_admin(dp: Dispatcher):
	dp.register_message_handler(start, lambda message:"Загрузить" in message.text, state=None)
	dp.register_message_handler(cancel, lambda message:"Отмена" in message.text, state=None)
	dp.register_message_handler(photo, content_types=["photo"],state=FSMAdmin.photo)
	dp.register_message_handler(name, state=FSMAdmin.name)
	dp.register_message_handler(desc, state=FSMAdmin.description)
	dp.register_message_handler(price, state=FSMAdmin.price)
	dp.register_message_handler(make_changes, commands=["moder"], is_chat_admin=True)