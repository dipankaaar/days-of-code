students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        students.append({"name": name, "age": age})
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found!")
        else:
            for s in students:
                print(s)

    elif choice == "3":
        search = input("Enter name to search: ")
        found = False
        for s in students:
            if s["name"] == search:
                print("Found:", s)
                found = True
        if not found:
            print("Student not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")
        students = [s for s in students if s["name"] != name]
        print("Student deleted (if existed)")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")