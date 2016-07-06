# Add table


import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create new table
    c.execute("""CREATE TABLE orders
                 (make TEXT, model TEXT, order_date DATE)""")

    cars = [

            ('ford', 'focus', '2016-05-05'),
            ('ford', 'focus', '2016-05-04'),
            ('ford', 'focus', '2016-06-06'),
            ('ford', 'focus', '2016-07-01'),
            ('ford', 'focus', '2016-08-01'),
            ('honda', 'accord', '2016-09-01'),
            ('honda', 'accord', '2015-08-10'),
            ('honda', 'accord', '2014-01-01'),
            ('honda', 'accord', '2013-01-01'),
            ('honda', 'accord', '2012-06-06'),
            ('honda', 'civic', '2016-07-08'),
            ('honda', 'civic', '2014-08-08'),
            ('ford', 'bronco', '2016-04-02'),
            ('ford', 'bronco', '2016-02-02'),
            ('ford', 'bronco', '2016-05-08')
            ]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", cars)
    c.execute("""SELECT i.make, i.model, i.quantity, o.order_date 
                 FROM orders AS o
                 INNER JOIN inventory as i
                 ON o.model = i.model
                    AND
                    o.make = i.make
              """)

    rows = c.fetchall()

    for r in rows:
        print r[0] + " " + r[1]
        print "Quantity: " + str(r[2])
        print "Order Date: " + r[3]
        print 