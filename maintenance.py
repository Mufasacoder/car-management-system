class Maintenance:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def add_maintenance(self):
        car_id = input("Enter car ID: ")
        date = input("Enter date of maintenance (YYYY-MM-DD): ")
        description = input("Enter maintenance description: ")
        cost = input("Enter cost: ")
        self.cursor.execute("INSERT INTO maintenance (car_id, date, description, cost) VALUES (?, ?, ?, ?)", (car_id, date, description, cost))
        self.conn.commit()
        print("Maintenance record added successfully!")
