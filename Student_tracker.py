students = {
    "ankit": {"math": 90, "english": 98, "physics": 96},
    "subham": {"math": 97, "english": 96, "physics": 95},
    "Subha": {"math": 96, "english": 94, "physics": 97},
    "mark": {"math": 91, "english": 92, "physics": 98},
    "chinki": {"math": 98, "english": 96, "physics": 92},
    "hardeep": {"math": 99, "english": 96, "physics": 98}
}

def add_student():
    name = input("Enter student name: ")
    math = int(input("Enter marks in math: "))
    english = int(input("Enter marks in English: "))
    physics = int(input("Enter marks in physics: "))
    students[name] = {"math": math, "english": english, "physics": physics}
    print("Student added.")

def update_student():
    name = input("Enter student name to update: ")
    if name in students:
        math = int(input("Enter new marks in math: "))
        english = int(input("Enter new marks in English: "))
        physics = int(input("Enter new marks in physics: "))
        students[name] = {"math": math, "english": english, "physics": physics}
        print(name,"data has been updated.")
    else:
        print("No student found with the name",name)

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Student",name,"Deleted")
    else:
        print("No student found with the name",name)

def view_students():
    print("\nCurrent Student Data:")
    for name, scores in students.items():
        print("Name:", name, "Math:", scores["math"], "English:", scores["english"], "Physics:", scores["physics"])


        
def __main__():
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
            print("Invalid option")

__main__()
