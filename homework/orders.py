import sqlite3


orders = (('Ford', 'Fiesta', '2016-03-05'),
		('Ford', 'Fiesta', '2016-12-12'),
		('Ford', 'Fiesta', '2017-01-01'),
		
		('Honda', 'Accord', '2015-09-23'),
		('Honda', 'Accord', '2017-11-02'),
		('Honda', 'Accord', '2016-10-25'),
		
		('Honda', 'CR-V', '2017-04-20'),
		('Honda', 'CR-V', '2017-11-09'),
		('Honda', 'CR-V', '2016-12-21'),

		('Ford', 'Mondeo', '2017-01-01'),
		('Ford', 'Mondeo', '2016-12-31'),
		('Ford', 'Mondeo', '2017-02-28'),

		('Ford', 'Mustang', '2015-09-27'),
		('Ford', 'Mustang', '2016-03-07'),
		('Ford', 'Mustang', '2015-05-22')

	)


with sqlite3.connect("cars.db") as connection :
	
	cursor = connection.cursor()
	cursor.executescript("""
		DROP TABLE IF EXISTS Orders;
		CREATE TABLE Orders(Make TEXT, Model TEXT, Order_date TEXT);""")
	cursor.executemany("INSERT INTO Orders VALUES(?, ?, ?)", orders)
	cursor.execute("""SELECT DISTINCT inventory.make, inventory.model,inventory.quantity, 
		orders.order_date FROM Orders, Inventory WHERE orders.model = inventory.model 
		ORDER BY orders.model ASC""")

	rows = cursor.fetchall()

	for i, r in enumerate(rows):
		if i % 3 == 0 :
			print("\nMake and model: " + r[0] + " " + r[1])
			print("Quantity: " + str(r[2]))
			print("Order dates: ")
		print(r[3])



