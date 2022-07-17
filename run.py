from database import Database

# Opens database connection, creating file if not found
db = Database("data.db")

db.create_tables()

db.insert_customer("Emily", "Asquith", "62 Pear Tree Park")
db.insert_customer("Kate", "Harper", "36 Thomas Crescent")

db.insert_event("AtmosVR Opening Night", "17/07/2022")
db.insert_event("Concert", "21/08/2022")

db.insert_ticket("17/07/2022", "1", "2")

records = db.get_ticket_data("1")

for record in records:
    print(record)
    print(f"{record[1]} {record[2]} purchased ticket for {record[3]}")
