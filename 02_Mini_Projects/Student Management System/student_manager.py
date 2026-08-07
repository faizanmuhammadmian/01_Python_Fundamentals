from student import Student
from file_handler import save_students, load_students

students = load_students()


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

        save_students(students)

        print("Student Added Successfully!")

    except ValueError:

        print("Invalid Input")


def view_students():

    if len(students) == 0:

        print("No students found.")
        return

    for student in students:

        student.display()
        student.is_passed()

    print("-" * 30)
    print("Total Students:", len(students))


def search_student():

    search_id = int(input("Enter Student ID: "))

    for student in students:

        if student.id == search_id:

            student.display()
            student.is_passed()
            return

    print("Student Not Found")


def update_student():

    search_id = int(input("Enter Student ID: "))

    for student in students:

        if student.id == search_id:

            student.name = input("New Name: ")
            student.age = int(input("New Age: "))
            student.student_class = input("New Class: ")

            new_marks = int(input("New Marks: "))
            student.update_marks(new_marks)

            save_students(students)

            print("Student Updated Successfully!")
            return

    print("Student Not Found")


def delete_student():

    search_id = int(input("Enter Student ID: "))

    for student in students:

        if student.id == search_id:

            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":

                students.remove(student)

                save_students(students)

                print("Student Deleted Successfully!")

            else:

                print("Deletion Cancelled.")

            return

    print("Student Not Found")







































# from student import Student

# students = []



# def add_student():

#     student_id = int(input("ID: "))
#     name = input("Name: ")
#     age = int(input("Age: "))
#     student_class = input("Class: ")
#     marks = int(input("Marks: "))

#     student = Student(
#         student_id,
#         name,
#         age,
#         student_class,
#         marks
#     )

#     students.append(student)

#     print("Student Added")