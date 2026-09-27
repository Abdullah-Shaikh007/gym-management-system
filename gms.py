members = []


def add_member():
    member_id = len(members) + 1
    name = input("Enter member name: ")
    age = int(input("Enter age: "))
    phone = input("Enter phone number: ")
    plan = input("Enter membership plan: ")

    member = {
        "id": member_id,
        "name": name,
        "age": age,
        "phone": phone,
        "plan": plan
    }

    members.append(member)
    print("Member added successfully!")


def view_members():
    if not members:
        print("No members found.")
        return

    for member in members:
        print("\nID:", member["id"])
        print("Name:", member["name"])
        print("Age:", member["age"])
        print("Phone:", member["phone"])
        print("Plan:", member["plan"])


while True:
    print("\n===== GYM MANAGEMENT SYSTEM =====")
    print("1. Add Member")
    print("2. View Members")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_member()
    elif choice == "2":
        view_members()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
