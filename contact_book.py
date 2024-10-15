import json
import os

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.contacts = json.load(f)
        else:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts):
            print(f"{idx + 1}. {contact['name']} - {contact['phone']}")

    def search_contact(self, query):
        results = [c for c in self.contacts if query.lower() in c['name'].lower() or query in c['phone']]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"{contact['name']} - {contact['phone']}")
        else:
            print("No contacts found.")

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            }
            self.save_contacts()
            print("Contact updated.")
        else:
            print("Invalid contact number.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            removed_contact = self.contacts.pop(index)
            self.save_contacts()
            print(f"Contact '{removed_contact['name']}' deleted.")
        else:
            print("Invalid contact number.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)
        elif choice == '4':
            contact_manager.view_contacts()
            try:
                index = int(input("Enter contact number to update: ")) - 1
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact_manager.update_contact(index, name, phone, email, address)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            contact_manager.view_contacts()
            try:
                index = int(input("Enter contact number to delete: ")) - 1
                contact_manager.delete_contact(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
