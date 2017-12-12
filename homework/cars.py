import sqlite3


connection = sqlite3.connect("cars.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE Inventory (Make TEXT, Model TEXT, Quantity INT)")
connection.close()