import sqlite3

def get_page_views():
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		pages =cur.execute("select * from pages").fetchall()
	return pages

def get_button_press():
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		buttons = cur.execute("select * from buttons").fetchall()
	return buttons

def get_user_comments():
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		user_comments = cur.execute("select * from user_comments")

