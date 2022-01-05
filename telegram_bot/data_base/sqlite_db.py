import sqlite3 as sq


def start():
	global base, cur
	base = sq.connect("shop_coll.dp")
	cur = base.cursor()
	if base:
		print("data base connector OK!")
	base.execute("CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)")
	base.commit()

async def sql_add_cmd(state):
	async with state.proxy() as data:
		cur.execute("INSERT INTO menu VALUES (?, ?, ?, ?)", tuple(data.values()))
		base.comit()
