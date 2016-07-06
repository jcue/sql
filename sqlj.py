# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # insert multiple records using a tuple
    car_list = [
                 ('Ford', 'Focus', 10),
                 ('Ford', 'Explorer', 27),
                 ('Ford', 'Bronco', 150),
                 ('Honda','Civic', 25),
                 ('Honda', 'Accord', 200)
                ]      

    # insert data into table
    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', car_list)