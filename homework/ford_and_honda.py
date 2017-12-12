import sqlite3

cars = ( ('Ford', 'Fiesta', 34),
		('Honda', 'Accord', 20),
		('Honda', 'CR-V', 40),
		('Ford', 'Mondeo', 33),
		('Ford', 'Mustang', 22)
	)



with sqlite3.connect("cars.db") as connection :
	
	cursor = connection.cursor()
	cursor.executescript("""
		DROP TABLE IF EXISTS Inventory;
		CREATE TABLE Inventory(Make TEXT, Model TEXT, Quantity INT);""")
	cursor.executemany("INSERT INTO Inventory VALUES(?, ?, ?)", cars)
	cursor.execute("UPDATE  Inventory SET Quantity = 30 WHERE Model = 'Fiesta'")
	cursor.execute("UPDATE  Inventory SET Quantity = 25 WHERE Model = 'Accord'")

	cursor.execute("SELECT * FROM Inventory")
	rows = cursor.fetchall()


	print("All cars:")
	for r in rows:
		print(r[0], r[1], r[2])

	cursor.execute("SELECT * FROM Inventory WHERE Make = 'Ford'")
	rows = cursor.fetchall()

	print("\nOnly Ford cars:")
	for r in rows:
		print(r[0], r[1], r[2])