import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()


    c.execute("select * from inventory")

    rows = c.fetchall()

    for r in rows:
        print "Make and Model: "  + r[0], r[1]
        print "Quantity: " + str(r[2]) + "\n"

        # retrieve order_date for the current make and model
        c.execute("SELECT count(order_date) FROM orders WHERE make=? and model=?", (r[0], r[1]))

        # fetchone() retrieves one record from the query
        order_count = c.fetchone()[0]

        # output the order count to the screen
        print "Order Count: " + str(order_count)