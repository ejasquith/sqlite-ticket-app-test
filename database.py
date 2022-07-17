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

    def insert_customer(self, first_name, surname, address):
        """
        Inserts given values into customer table
        """
        with self.connection:
            self.connection.execute(
                "INSERT INTO customer VALUES (?, ?, ?);",
                (first_name, surname, address)
            )

    def insert_event(self, name, date):
        """
        Inserts given values into event table
        """
        with self.connection:
            self.connection.execute(
                "INSERT INTO event VALUES (?, ?);",
                (name, date)
            )

    def insert_ticket(self, date_purchased, customer_id, event_id):
        """
        Inserts given values into ticket table
        """
        with self.connection:
            self.connection.execute(
                "INSERT INTO ticket VALUES (?, ?, ?)",
                (date_purchased, customer_id, event_id)
            )

    def get_ticket_data(self, ticket_id):
        """
        Retrieves ticket and linked customer and event data
        """
        with self.connection:
            return self.connection.execute(
                """SELECT ticket.rowid, customer.first_name, customer.surname, event.event_name
                   FROM ticket
                   WHERE ticket.rowid = ?
                   INNER JOIN customer ON customer.rowid = ticket.customer_id,
                   INNER JOIN event ON event.rowid = ticket.event_id;
                """,
                (ticket_id)
            )
