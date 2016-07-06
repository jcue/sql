

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # update data
    c.execute("UPDATE inventory SET Quantity = 100 WHERE Model ='Bronco'")
    c.execute("UPDATE inventory SET Quantity = 221 WHERE Model = 'Accord'")

    print "\nNEW DATA: \n"

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]

