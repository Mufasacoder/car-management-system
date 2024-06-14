class Car:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def add_car(self):
        make = input("Enter make: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        vin = input("Enter VIN: ")
        self.cursor.execute("INSERT INTO cars (make, model, year, vin) VALUES (?, ?, ?, ?)", (make, model, year, vin))
        self.conn.commit()
        print("Car added successfully!")

    def display_cars(self):
        self.cursor.execute("SELECT * FROM cars")
        cars = self.cursor.fetchall()
        print("Cars:")
        for car in cars:
            print(car)

    def search_car(self, make=None, model=None, vin=None):
        query = "SELECT * FROM cars WHERE "
        args = []
        conditions = []
        if make:
            conditions.append("make = ?")
            args.append(make)
        if model:
            conditions.append("model = ?")
            args.append(model)
        if vin:
            conditions.append("vin = ?")
            args.append(vin)
        query += " AND ".join(conditions)
        self.cursor.execute(query, args)
        cars = self.cursor.fetchall()
        return cars
    def update_car(self, car_id, make=None, model=None, year=None, vin=None):
        update_query = "UPDATE cars SET"
        args = []
        if make:
            update_query += " make=?,"
            args.append(make)
        if model:
            update_query += " model=?,"
            args.append(model)
        if year:
            update_query += " year=?,"
            args.append(year)
        if vin:
            update_query += " vin=?,"
            args.append(vin)
        update_query = update_query[:-1] + " WHERE id=?"
        args.append(car_id)
        self.cursor.execute(update_query, args)
        self.conn.commit()

    def delete_car(self, car_id):
        self.cursor.execute("DELETE FROM cars WHERE id=?", (car_id,))
        self.conn.commit()

    def generate_report(self):
        self.cursor.execute("SELECT make, model, COUNT(*) as total FROM cars GROUP BY make, model")
        report = self.cursor.fetchall()
        return report

    def get_maintenance_cost(self, car_id):
        self.cursor.execute("SELECT SUM(cost) FROM maintenance WHERE car_id=?", (car_id,))
        total_cost = self.cursor.fetchone()[0]
        return total_cost
