class Owner:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def add_owner(self):
        car_id = input("Enter car ID: ")
        name = input("Enter owner's name: ")
        contact = input("Enter owner's contact: ")
        purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
        self.cursor.execute("INSERT INTO owners (car_id, name, contact, purchase_date) VALUES (?, ?, ?, ?)", (car_id, name, contact, purchase_date))
        self.conn.commit()
        print("Owner added successfully!")
