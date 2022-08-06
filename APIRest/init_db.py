from multiprocessing import connection
import sqlite3

connection= sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur= connection.cursor()

cur.execute("INSERT INTO StatusOrders(name) VALUES(?)", ('Pending', ))
cur.execute("INSERT INTO StatusOrders(name) VALUES(?)", ('In Process', ))
cur.execute("INSERT INTO StatusOrders(name) VALUES(?)", ('Completed', ))
cur.execute("INSERT INTO StatusOrders(name) VALUES(?)", ('Delivered', ))
cur.execute("INSERT INTO StatusOrders(name) VALUES(?)", ('Canceled', ))


connection.commit()
connection.close()

