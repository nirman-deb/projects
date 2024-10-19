students = [
    ["ankit", 90, 98, 96],
    ["subham", 97, 96, 95],
    ["Subha", 96, 94, 97],
    ["mark", 91, 92, 98],
    ["chinki",98,96,92],
    ["hardeep",99,96,98]
]

def add_student():
    name = input("Enter student name: ")
    math = int(input("Enter marks in math: "))
    english = int(input("Enter marks in English: "))
    physics = int(input("Enter marks in physics: "))
    students.append([name, math, english, physics])
    print("Student",name, " added.")

def update_student():
    name = input("Enter student name to update: ")
    for student in students:
        if student[0] == name:
            math = int(input("Enter new marks in math: "))
            english = int(input("Enter new marks in English: "))
            physics = int(input("Enter new marks in physics: "))
            student[1] = math
            student[2] = english
            student[3] = physics
            print(name,"s data has been updated.")
    else:
        print("No student found with the name",name)

def delete_student():
    name = input("Enter student name to delete: ")
    for student in students:
        if student[0] == name:
            students.remove(student)
            print("Student",name, "Deleted")
    else:
        print("No student found with the name",name)

def view_students():
    print("Current Student Data:")
    for student in students:
        print(student[0], student[1], student[2], student[3])

def main():
    while True:
        print("\nStudent Exam Scores Tracker")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            break
        else:
            print("Invalid option.")
main()
