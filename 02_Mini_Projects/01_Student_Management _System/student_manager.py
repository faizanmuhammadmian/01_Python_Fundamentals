import json

from student import Student

students = []


# -------------------------------
# Load Students
# -------------------------------

def load_students():

    global students

    try:

        with open("students.json", "r") as file:

            data = json.load(file)

            students = []

            for item in data:

                student = Student(
                    item["id"],
                    item["name"],
                    item["age"],
                    item["class"],
                    item["marks"]
                )

                students.append(student)

    except FileNotFoundError:

        students = []


# -------------------------------
# Save Students
# -------------------------------

def save_students():

    data = []

    for student in students:

        data.append(student.to_dict())

    with open("students.json", "w") as file:

        json.dump(data, file, indent=4)


# -------------------------------
# Add Student
# -------------------------------

def add_student():

    try:

        student_id = int(input("Enter ID: "))

        for student in students:

            if student.id == student_id:

                print("Student ID already exists!")
                return

        name = input("Enter Name: ")

        age = int(input("Enter Age: "))

        student_class = input("Enter Class: ")

        marks = int(input("Enter Marks: "))

        student = Student(
            student_id,
            name,
            age,
            student_class,
            marks
        )

        students.append(student)

        save_students()

        print("Student Added Successfully!")

    except ValueError:

        print("Invalid Input.")


# -------------------------------
# View Students
# -------------------------------

def view_students():

    if len(students) == 0:

        print("No Students Found")

        return

    for student in students:

        student.display()

    print("\nTotal Students:", len(students))


# -------------------------------
# Search Student
# -------------------------------

def search_student():

    search_id = int(input("Enter Student ID: "))

    for student in students:

        if student.id == search_id:

            student.display()

            return

    print("Student Not Found")


# -------------------------------
# Update Student
# -------------------------------

def update_student():

    search_id = int(input("Enter Student ID: "))

    for student in students:

        if student.id == search_id:

            student.name = input("New Name: ")

            student.age = int(input("New Age: "))

            student.student_class = input("New Class: ")

            marks = int(input("New Marks: "))

            student.update_marks(marks)

            save_students()

            print("Student Updated Successfully!")

            return

    print("Student Not Found")


# -------------------------------
# Delete Student
# -------------------------------

def delete_student():

    search_id = int(input("Enter Student ID: "))

    for student in students:

        if student.id == search_id:

            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":

                students.remove(student)

                save_students()

                print("Student Deleted Successfully!")

            else:

                print("Deletion Cancelled")

            return

    print("Student Not Found")