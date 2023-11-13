#initialize an empty contacts dictionary to store contact information
contacts = {}

# function to add a new contact
def add_contact():
    name = input("Enter the name:")
    phone = input("Enter the phone number:")
    email = input("Enter the email:")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"contact '{name}' added successfully!")

# Function to view contact details
def view_contact(name):
    if name in contacts:
        contact_info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact_info['Phone']}")
        print(f"Email: {contact_info['Email']}")
    else:
        print(f"Contact '{name}' not found!")
# Function to list all contacts
def list_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("List of Contacts:")
        for name in contacts:
            print(name)

# Main program loop
while True:
    print("\nContact Application Menu:")
    print("1. Add a contact")
    print("2. View a contact")
    print("3. List all contacts")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        name = input("Enter the name of the contact: ")
        view_contact(name)
    elif choice == "3":
        list_contacts()
    elif choice == "4":
        print("Exiting the Contact Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
