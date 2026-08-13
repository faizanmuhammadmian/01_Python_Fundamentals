from student_manager import *

from utils import print_line


load_students()


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