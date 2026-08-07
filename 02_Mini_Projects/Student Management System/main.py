from utils import print_line
from student_manager import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

while True:

    print_line()
    print("STUDENT MANAGEMENT SYSTEM")
    print_line()

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        update_student()

    elif choice == "5":

        delete_student()

    elif choice == "6":

        print("Good Bye!")
        break

    else:

        print("Invalid Choice")











































# from utils import print_line
# from student_manager import *



# while True:

#     print("1 Add")
#     print("2 View")
#     print("3 Exit")

#     choice = input()

#     if choice == "1":

#         add_student()

#     elif choice == "2":

#         for student in students:

#             student.display()

#     elif choice == "3":

#         break


