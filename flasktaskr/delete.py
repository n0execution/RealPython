from project._config import DATABASE_PATH

import sqlite3
from datetime import datetime

with sqlite3.connect(DATABASE_PATH) as connection :
    # get a cursor object used to execute SQL commands
	cursor = connection.cursor()
	cursor.execute("""DELETE FROM Users""")
