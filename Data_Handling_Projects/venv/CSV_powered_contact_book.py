"""
CLI Contact Book (CSV_Powered)

Created a terminal-based contact book tool that stores and manages contacts using a CSV file.

"""
import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    #check for duplicates
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists")
                return
        
    with open(FILENAME, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added")

def view_contacts():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 1:
            print("No contacts")
            return
        
        print("\nYour contacts: \n")
        for row in rows:
            if len(row) < 3:
                continue
            print(f"{row[0]} | {row[1]} | {row[2]}")
        

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row["Name"]} | {row["Phone"]}")
                found = True

    if not found:
        print("No matching contact found")


def main():
    while True:
        choice = int(input("\nChoose one of the following: \n1. Add a new contact \n2. View all contacts \n3. Search for a contact by name \n4. Exit\n"))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            print("Thanks for using our software")
            break
        else:
            print("Invalid option!")
            
if __name__ == "__main__":
    main()

