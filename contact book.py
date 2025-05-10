def add_contact():
    name = input("Enter name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    # Ensure no blank fields
    if not name or not phone_number or not email:
        print("All fields are required.")
        return

    with open("contact list.txt", "a") as file:
        file.write(f"{name} | {phone_number} | {email}\n")  # only one \n

    print("Contact added successfully.")



def view_contacts():
    try:
        with open("contact list.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No contacts found.")
                return

            print("\n--- Contact List ---")
            for line in lines:
                line = line.strip()
                if not line:
                    continue  # Skip truly empty lines

                parts = [part.strip() for part in line.split("|")]
                if len(parts) == 3:
                    name, phone_number, email = parts
                    print(f"NAME: {name} | PHONE: {phone_number} | EMAIL: {email}")
                else:
                    print(f" Skipping invalid line: {line}")
    except FileNotFoundError:
        print("No contacts found.")


def search_contact():
    search = input("Enter name to search: ").strip().lower()
    found = False

    try:
        with open("contact list.txt", "r") as file:
            for line in file:
                parts = [part.strip() for part in line.strip().split("|")]
                if len(parts) == 3:
                    name, phone_number, email = parts
                    if search == name.lower():
                        print(f"NAME: {name} | PHONE: {phone_number} | EMAIL: {email}")
                        found = True
                        break
        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts found.")


def delete_contact():
    delete_name = input("Enter name to delete: ").strip().lower()
    found = False

    try:
        with open("contact list.txt", "r") as file:
            lines = file.readlines()

        with open("contact list.txt", "w") as file:
            for line in lines:
                parts = [part.strip() for part in line.strip().split("|")]
                if len(parts) == 3:
                    name, phone_number, email = parts
                    if delete_name != name.lower():
                        file.write(line)
                    else:
                        found = True
                else:
                    file.write(line)  # Keep invalid lines

        if found:
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts found.")


# Main loop
while True:
    print("\n---- Welcome to Contact Book ----")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
