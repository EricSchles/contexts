import sqlite3

def get_entries():
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		entries = cur.execute("select * from entries").fetchall()
		return entries