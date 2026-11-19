import student

print("Welcome to Student Management System")
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
    print("5. Delete Student")

    choice = input("Enter your choice: ")

    if choice == "1":
        student.add_student()

    elif choice == "2":
        student.display_students()

    elif choice == "3":
        student.search_student()

    elif choice == "4":
        print("Exiting program...")
        break
        
    elif choice == "5":
    	student.delete_student()

    else:
        print("Invalid choice! Try again.")
