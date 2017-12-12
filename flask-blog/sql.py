import sqlite3


with sqlite3.connect("blog.db") as connection :
	cursor = connection.cursor()
	cursor.executescript("""DROP TABLE IF EXISTS posts;
						CREATE TABLE posts (title TEXT, post TEXT);""")
	cursor.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
	cursor.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
	cursor.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')