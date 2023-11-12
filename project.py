#initialize an empty contacts dictionary to store contact information
contacts = {}

# function to add a new contact
def add_contact():
    name = input("Enter the name:")
    phone = input("Enter the phone number:")
    email = input("Enter the email:")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"contact '{name}' added successfully!")