import sqlite3



with sqlite3.connect("cars.db") as connection :
	
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM Inventory")
	rows = cursor.fetchall()

	for r in rows :
		cursor.execute("SELECT count(order_date) FROM Orders WHERE model = ?", (r[1],))
		print("Make and model: {} {} \nQuantity: {}\nOrders: {}\n".format(r[0], r[1], r[2], cursor.fetchone()[0]))
