from database import Database

# Opens database connection, creating file if not found
db = Database("data.db")

db.create_tables()
