students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")

def display_students():
    if not students:
        print("No students found.")
    else:
        for s in students:
            print("\nRoll Number:", s["roll"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Course:", s["course"])

def search_student():
    roll = input("Enter Roll Number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found!")
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Course:", s["course"])
            return

    print("Student not found.")
