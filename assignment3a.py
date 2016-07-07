# Example Application

import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete database table if exist
    c.execute("DROP TABLE if exists numbers")

    # create database table
    c.execute("CREATE TABLE numbers(num int)")

    for x in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", ( random.randint(0,100), ))

