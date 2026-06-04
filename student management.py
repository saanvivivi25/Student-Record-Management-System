def add_student(students):

    name = input("Enter Student Name: ")

    while True:
        try:
            marks = float(input("Enter Marks: "))

            if marks >= 0 and marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter numeric values only.")

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully.\n")


def view_students(students):

    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\n----- STUDENT RECORDS -----")

    for student in students:
        print("Name :", student["name"])
        print("Marks:", student["marks"])
        print("-" * 25)


def highest_student(students):

    if len(students) == 0:
        print("No student records available.\n")
        return

    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    print("\nHighest Scoring Student")
    print("Name :", highest["name"])
    print("Marks:", highest["marks"])
    print()


def class_average(students):

    if len(students) == 0:
        print("No student records available.\n")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Class Average:", round(average, 2))
    print()


def display_menu():

    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Find Highest Scoring Student")
    print("4. Calculate Class Average")
    print("5. Exit")


# Main Program

students = []

while True:

    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        highest_student(students)

    elif choice == "4":
        class_average(students)

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice. Please try again.\n")