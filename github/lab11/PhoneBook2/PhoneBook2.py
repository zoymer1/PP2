import csv
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Oitel.arni2004",
        database="Phonebook_db2"
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

def call_pattern_function():
    pattern = input("Enter pattern to search: ")
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT get_users_by_pattern(%s)", (pattern,))
        result = cursor.fetchone()[0]
        print("Results:", result if result else "No matches found.")

def call_insert_procedure():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        cursor = conn.cursor()
        cursor.callproc('insert_or_update_user', (name, phone))
        print("✔ Done")

def call_insert_many_procedure():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.callproc('insert_multiple_users')
        print("✔ Multiple users inserted (check for any invalid entries in console)")

def call_paginate_function():
    offset = int(input("Offset: "))
    limit = int(input("Limit: "))
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT paginate_users(%s, %s)", (offset, limit))
        result = cursor.fetchone()[0]
        print("Page result:", result if result else "No entries.")

def call_delete_procedure():
    name = input("Enter name to delete (or leave blank): ")
    phone = input("Enter phone to delete (or leave blank): ")
    with connect() as conn:
        cursor = conn.cursor()
        cursor.callproc('delete_user_by_name_or_phone', (name or None, phone or None))
        print("✔ Deleted")

def main():
    create_table()
    while True:
        print("\nPHONEBOOK MENU")
        print("1. Insert user from console")
        print("2. Insert users from CSV file")
        print("3. Update user")
        print("4. Query users")
        print("5. Delete user")
        print("6. Search pattern (function)")
        print("7. Insert with procedure")
        print("8. Insert many with looped procedure")
        print("9. Pagination (function)")
        print("10. Delete with procedure")
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
        elif choice == "6":
            call_pattern_function()
        elif choice == "7":
            call_insert_procedure()
        elif choice == "8":
            call_insert_many_procedure()
        elif choice == "9":
            call_paginate_function()
        elif choice == "10":
            call_delete_procedure()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
