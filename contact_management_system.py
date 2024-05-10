class Contact:
  def __init__(self, name, phone_number, email):
    self.name = name
    self.phone_number = phone_number
    self.email = email

# Create a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact(name, phone_number, email):
  if name not in contacts:
    contacts[name] = Contact(name, phone_number, email)
    print(f"Contact '{name}' added successfully.")
  else:
    print(f"Contact '{name}' already exists.")

# Function to update contact information
def update_contact(name):
  if name in contacts:
    new_phone_number = input("Enter new phone number: ")
    new_email = input("Enter new email: ")
    contacts[name].phone_number = new_phone_number
    contacts[name].email = new_email
    print(f"Contact '{name}' updated successfully.")
  else:
    print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact(name):
  if name in contacts:
    del contacts[name]
    print(f"Contact '{name}' deleted successfully.")
  else:
    print(f"Contact '{name}' not found.")

# Function to display all contacts
def list_contacts():
  if contacts:
    for name, contact in contacts.items():
      print(f"- {name}: {contact.phone_number}, {contact.email}")
  else:
    print("No contacts found.")

# Main loop
while True:
  print("\nMenu:")
  print("1. Add Contact")
  print("2. Update Contact")
  print("3. Delete Contact")
  print("4. List Contacts")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    add_contact(name, phone_number, email)
  elif choice == "2":
    name = input("Enter name of contact to update: ")
    update_contact(name)
  elif choice == "3":
    name = input("Enter name of contact to delete: ")
    delete_contact(name)
  elif choice == "4":
    list_contacts()
  elif choice == "5":
    break
  else:
    print("Invalid choice.")
