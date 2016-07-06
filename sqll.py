import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# Return all cars that are fords
	c.execute("SELECT * FROM inventory WHERE Make = 'Ford'")

	print "\Ford Cars: \n"

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]