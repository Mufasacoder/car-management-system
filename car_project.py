import sqlite3
from car import Car
from maintenance import Maintenance
from owner import Owner

# Function to connect to the SQLite database
def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn

# Function to create tables if they don't exist
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                        id INTEGER PRIMARY KEY,
                        make TEXT NOT NULL,
                        model TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        vin TEXT UNIQUE NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS maintenance (
                        id INTEGER PRIMARY KEY,
                        car_id INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        description TEXT NOT NULL,
                        cost REAL NOT NULL,
                        FOREIGN KEY (car_id) REFERENCES cars(id)
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS owners (
                        id INTEGER PRIMARY KEY,
                        car_id INTEGER NOT NULL,
                        name TEXT NOT NULL,
                        contact TEXT NOT NULL,
                        purchase_date TEXT NOT NULL,
                        FOREIGN KEY (car_id) REFERENCES cars(id)
                    )''')
    conn.commit()

# Main function
def main():
    db_name = "car_project.db"
    conn = connect_db(db_name)

    # Create tables if they don't exist
    create_tables(conn)

    # Create instances of Car, Maintenance, and Owner classes
    car_instance = Car(conn)
    maintenance_instance = Maintenance(conn)
    owner_instance = Owner(conn)

    while True:
        print("\n1. Add a car")
        print("2. Add maintenance record")
        print("3. Add owner")
        print("4. Display all cars")
        print("5. Search for a car")
        print("6. Update a car")
        print("7. Delete a car")
        print("8. Generate report")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            car_instance.add_car()

        elif choice == "2":
            maintenance_instance.add_maintenance()

        elif choice == "3":
            owner_instance.add_owner()

        elif choice == "4":
            car_instance.display_cars()

        elif choice == "5":
            make = input("Enter make (optional): ")
            model = input("Enter model (optional): ")
            vin = input("Enter VIN (optional): ")
            cars = car_instance.search_car(make, model, vin)
            print("Search Results:")
            for car in cars:
                print(car)

        elif choice == "6":
            car_id = input("Enter car ID to update: ")
            make = input("Enter new make (optional): ")
            model = input("Enter new model (optional): ")
            year = input("Enter new year (optional): ")
            vin = input("Enter new VIN (optional): ")
            car_instance.update_car(car_id, make, model, year, vin)
            print("Car updated successfully!")

        elif choice == "7":
            car_id = input("Enter car ID to delete: ")
            car_instance.delete_car(car_id)
            print("Car deleted successfully!")

        elif choice == "8":
            report = car_instance.generate_report()
            print("Car Report:")
            for entry in report:
                print(f"{entry[0]} {entry[1]}: {entry[2]} cars")

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    conn.close()

if __name__ == "__main__":
    main()
