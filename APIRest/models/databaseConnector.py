import sqlite3

class databaseConnector:
    def get_db_connection():
        conn=sqlite3.connect('database.db')
        conn.row_factory=sqlite3.Row
        return conn