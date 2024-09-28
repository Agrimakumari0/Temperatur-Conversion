# Simple Contact Management System

contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

def edit_contact():
    view_contacts()
    if not contacts:
        return
    contact_number = int(input("Enter the contact number to edit: ")) - 1
    if contact_number < 0 or contact_number >= len(contacts):
        print("Invalid contact number!")
        return
    contact = contacts[contact_number]
    contact['name'] = input(f"Enter new name (leave blank to keep '{contact['name']}'): ") or contact['name']
    contact['phone'] = input(f"Enter new phone (leave blank to keep '{contact['phone']}'): ") or contact['phone']
    contact['email'] = input(f"Enter new email (leave blank to keep '{contact['email']}'): ") or contact['email']
    print(f"Contact {contact_number + 1} updated successfully!")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    contact_number = int(input("Enter the contact number to delete: ")) - 1
    if contact_number < 0 or contact_number >= len(contacts):
        print("Invalid contact number!")
        return
    removed_contact = contacts.pop(contact_number)
    print(f"Contact {removed_contact['name']} deleted successfully!")

def menu():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
menu()