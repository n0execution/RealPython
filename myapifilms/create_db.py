# Create a SQLite3 database and table
import sqlite3

with sqlite3.connect("movies.db") as connection:
    c = connection.cursor()

# create a table
c.executescript("""DROP TABLE IF EXISTS new_movies;
    CREATE TABLE new_movies (title TEXT, year INT, simplePlot text, 
                                    release_date text,  
                                    type INT)""")