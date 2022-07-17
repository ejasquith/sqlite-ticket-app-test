import sqlite3


class Database:
    """
    Creates an object used to handle connection to a particular database
    """
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = sqlite3.connect(connection_string)

    def create_tables(self):
        """
        Creates initial tables in database
        """
        with self.connection:
            self.connection.execute(
                """CREATE TABLE IF NOT EXISTS customer
                   (first_name TEXT, surname TEXT, address TEXT);"""
            )
            self.connection.execute(
                """CREATE TABLE IF NOT EXISTS event
                   (name TEXT, date TEXT);"""
            )
            self.connection.execute(
                """CREATE TABLE IF NOT EXISTS ticket
                   (customer_id INTEGER, event_id INTEGER,
                    date_purchased TEXT,
                    FOREIGN KEY(customer_id) REFERENCES customer(rowid),
                    FOREIGN KEY(event_id) REFERENCES event(rowid));"""
            )
