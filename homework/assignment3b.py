import sqlite3

class WrongNumber(Exception):
    pass

operations = {
	1 : "SELECT AVG(num) FROM numbers",
	2 : "SELECT MAX(num) FROM numbers",
	3 : "SELECT MIN(num) FROM numbers",
	4 : "SELECT SUM(num) FROM numbers",
}


with sqlite3.connect("newnum.db") as connection :
	cursor = connection.cursor()

	while True :
		print("Enter a number between 1-4 to perform operations with table or 0 to exit.")
		print("""Operations: 
1. Average
2. Maximum
3. Minimum
4. Sum""")
		
		try :
			choice = int(input())
			if (choice) not in range (5) :
				raise WrongNumber()
		except (ValueError, WrongNumber) as e :
		
			if type(e).__name__ == "ValueError" :
				print("Enter only numbers!\n")
			else :
				print("Wrong number\n")


		if choice == 0 :
			break

		cursor.execute(operations[choice])
		number = cursor.fetchone()[0]
		print("{}\n".format(number))



