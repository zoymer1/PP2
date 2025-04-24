import csv
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Oitel.arni2004",
        database="Phonebook_db"
    )

def create_table():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                phone VARCHAR(20)
            )
        """)
        conn.commit()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("✔ Inserted")

def insert_from_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile, connect() as conn:
            reader = csv.reader(csvfile)
            cursor = conn.cursor()
            for row in reader:
                if len(row) >= 2:
                    cursor.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
            conn.commit()
            print("CSV data inserted")
    except FileNotFoundError:
        print("File not found")

def update_user():
    old_name = input("Enter current name of user: ")
    new_name = input("Enter new name (or press Enter to skip): ")
    new_phone = input("Enter new phone (or press Enter to skip): ")
    with connect() as conn:
        cursor = conn.cursor()
        if new_name:
            cursor.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
        if new_phone:
            cursor.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, new_name or old_name))
        conn.commit()
        print("Updated")

def query_users():
    name = input("Filter by name (or press Enter to skip): ")
    phone = input("Filter by phone (or press Enter to skip): ")
    with connect() as conn:
        cursor = conn.cursor()
        if name:
            cursor.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
        elif phone:
            cursor.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
        else:
            cursor.execute("SELECT * FROM phonebook")
        rows = cursor.fetchall()
        print("Phonebook entries:")
        for row in rows:
            print(row)
        if not rows:
            print("No results found.")

def delete_user():
    name = input("Delete by name (or press Enter to skip): ")
    phone = input("Delete by phone (or press Enter to skip): ")
    with connect() as conn:
        cursor = conn.cursor()
        if name:
            cursor.execute("DELETE FROM phonebook WHERE name = %s", (name,))
        if phone:
            cursor.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        conn.commit()
        print("Deleted")

def main():
    create_table()
    while True:
        print("PHONEBOOK MENU")
        print("1. Insert user from console")
        print("2. Insert users from CSV file")
        print("3. Update user")
        print("4. Query users")
        print("5. Delete user")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            path = input("Enter CSV file path: ")
            insert_from_csv(path)
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_users()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()