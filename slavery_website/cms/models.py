import sqlite3

def get_entries():
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		entries = cur.execute("select * from entries").fetchall()
		return entries

def add_entry(entry):
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("insert into entries (entry) values (?)", entry)
		con.commit()

def remove_entry(id):
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		query = "delete from entries where id = '%s';" % id.strip()
		cur.execute(query)
