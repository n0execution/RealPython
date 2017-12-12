import sqlite3


connection = sqlite3.connect("new.db")

cursor = connection.cursor()


try:
	
	cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
	cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")
	
	conn.commit()

except sqlite3.OperationalError as e :
	print("Oops! Error: {} \nTry again...".format(e))

connection.close()