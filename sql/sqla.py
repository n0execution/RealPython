import sqlite3


cities = (
		('Kyiv', 'Ukraine', 2900920),
		('Barcelona', 'Spain', 1611822 ),
		('Vienna', 'Austria', 1867582),
		('Mexico', 'Mexica', 8918653),
		('Capetown', 'SAR', 433688),
		('Cairo', 'Egypt', 8026454),
		('Buenos Aires', 'Argentina', 3054300),
		('Tokyo', 'Japan', 13185502)
		)



connection = sqlite3.connect("new.db")

cursor = connection.cursor()

cursor.executescript("""
		DROP TABLE IF EXISTS Population;
		CREATE TABLE Population (city TEXT, state TEXT, population INT);""")

cursor.executemany("INSERT INTO Population VALUES(?, ?, ?)", cities)

connection.commit()
connection.close()