import sqlite3
import random




with sqlite3.connect("newnum.db") as connection :
	cursor = connection.cursor()
	cursor.executescript("""DROP TABLE IF EXISTS numbers;
						CREATE TABLE numbers (num INT);""")
	for i in range(100) :
		number = random.randint(0, 100)
		cursor.execute("INSERT INTO numbers VALUES(?)", (number, ))
