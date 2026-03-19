contacts={}

def add_contact():
    name=input("Enter  name:")
    phone_no=input("Enter the phone number:")
    Email=input("Enter the email:")
    address=input("Enter the address:")

    contacts[name]={"Phone No":phone_no,"Email":Email,"Address":address}

    print("contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("Contact List:")
    for name,info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone No: {info['Phone No']}")
        print(f"Email: {info['Email']}")
        print(f"Address: {info['Address']}")
        return

def search_contact():
    key = input("Enter name or phone to search: ")

    for name, info in contacts.items():
        if key == name or key == info["phone"]:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", info["phone"])
            print("Email:", info["email"])
            print("Address:", info["address"])
            return

    print("Contact not found.")

def update_contact():
    name=input("Enter the name of the contact toupdate:")

    if name in contacts:
        phone_no=input("Enter the new phone number:")
        Email=input("Enter the new email:")
        address=input("Enter the new address:")

        contacts[name]={"Phone No":phone_no,"Email":Email,"Address":address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name=input("Enter the name of the contact yo wnat to delete:")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\n======== Contact Book Menu ========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try:
        choice=int(input("Enter your choice:"))

        if choice==1:
            add_contact()

        elif choice==2:
            view_contacts()

        elif choice==3:
            search_contact()

        elif choice==4:
            update_contact()

        elif choice==5:
            delete_contact()

        elif choice==6:
            print("Exiting the contact book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")

