import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO population VALUES('New York City', \
	'NY', 8200000)")
	c.execute("INSERT INTO population VALUES('San Francisco', \
	'CA', 800000)")