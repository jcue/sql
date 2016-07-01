# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE inventory
				  (Make TEXT, Model Text, Quantity INT)
				  """)

# close teh database connection
conn.close()