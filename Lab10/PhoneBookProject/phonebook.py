import psycopg2
import csv
from db_config import config

def connect():
    return psycopg2.connect(**config)

def insert_from_csv():
    try:
        with connect() as conn, conn.cursor() as cur:
            with open('phonebook.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0
                for row in reader:
                    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                                (row['username'], row['phone']))
                    count += 1
            conn.commit()
            print(f"Inserted {count} entries from CSV")
    except Exception as e:
        print("Error loading from CSV:", e)

def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")
    with connect() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
        conn.commit()
        print(f"Inserted user {username}")

def update_user():
    username = input("Username to update: ")
    new_phone = input("New phone: ")
    with connect() as conn, conn.cursor() as cur:
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, username))
        if cur.rowcount == 0:
            print("No such user found.")
        else:
            conn.commit()
            print("Phone updated.")

def search():
    keyword = input("Enter username or phone to search: ")
    with connect() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook WHERE username = %s OR phone = %s", (keyword, keyword))
        results = cur.fetchall()
        if results:
            print("🔍 Results:")
            for row in results:
                print(f"ID: {row[0]}, Username: {row[1]}, Phone: {row[2]}")
        else:
            print("No matching records found.")

def delete():
    keyword = input("Enter username or phone to delete: ")
    with connect() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM phonebook WHERE username = %s OR phone = %s", (keyword, keyword))
        if cur.rowcount == 0:
            print("No matching records to delete.")
        else:
            conn.commit()
            print(f"Deleted {cur.rowcount} record(s).")

def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update")
        print("4. Search")
        print("5. Delete")
        print("6. Exit")
        choice = input("Choose: ")
        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_user()
        elif choice == '4':
            search()
        elif choice == '5':
            delete()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
