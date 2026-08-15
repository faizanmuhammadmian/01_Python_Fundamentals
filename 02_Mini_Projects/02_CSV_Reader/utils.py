def print_line():
    print("=" * 50)


def print_menu():
    print_line()
    print("        CSV Reader System")
    print_line()
    print("1. View Employees")
    print("2. Add Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Count Employees")
    print("7. Exit")
    print_line()


def get_valid_age():

    while True:

        try:

            age = int(input("Enter Age: "))

            if age > 0:
                return age

            print("Age must be greater than 0.")

        except ValueError:

            print("Please enter numbers only.")


def get_valid_salary():

    while True:

        try:

            salary = int(input("Enter Salary: "))

            if salary >= 0:
                return salary

            print("Salary cannot be negative.")

        except ValueError:

            print("Please enter numbers only.")