import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def display_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
    else:
        print("Contact List:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def add_contact(contacts, name, number):
    contacts[name] = number
    print(f"Contact '{name}' added successfully!")

def search_contact(contacts, name):
    if name in contacts:
        print(f"Contact Details - {name}: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n1. Display Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(contacts, name, number)
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(contacts, name)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            delete_contact(contacts, name)
        elif choice == '5':
            save_contacts(contacts)
            print("Contact book saved. Quitting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

