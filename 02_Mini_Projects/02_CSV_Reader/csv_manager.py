import csv

from utils import get_valid_age, get_valid_salary


class CSVManager:

    def __init__(self, filename):

        self.filename = filename

    # --------------------------

    def display(self):

        try:

            with open(self.filename, "r") as file:

                reader = csv.reader(file)

                for row in reader:
                    print(row)

        except FileNotFoundError:

            print("CSV File Not Found.")

    # --------------------------

    def add(self):

        employee_id = input("Enter ID: ")

        name = input("Enter Name: ").strip()

        department = input("Enter Department: ").strip()

        age = get_valid_age()

        salary = get_valid_salary()

        rows = []

        with open(self.filename, "r" ) as file:

            reader = csv.reader(file)

            rows = list(reader)

        for row in rows[1:]:

            if row[0] == employee_id:

                print("Employee ID Already Exists.")

                return

        with open(self.filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    employee_id,
                    name,
                    age,
                    department,
                    salary,
                ]
            )

        print("Employee Added Successfully.")

    # --------------------------

    def update(self):

        employee_id = input("Enter Employee ID: ")

        rows = []

        found = False

        with open(self.filename, "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

        for row in rows:

            if row[0] == employee_id:

                found = True

                print("Leave blank to keep old value.")

                new_name = input(f"Name ({row[1]}): ")

                new_age = input(f"Age ({row[2]}): ")

                new_department = input(f"Department ({row[3]}): ")

                new_salary = input(f"Salary ({row[4]}): ")

                if new_name:
                    row[1] = new_name

                if new_age:
                    row[2] = new_age

                if new_department:
                    row[3] = new_department

                if new_salary:
                    row[4] = new_salary

                break

        if not found:

            print("Employee Not Found.")

            return

        with open(self.filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)

        print("Employee Updated Successfully.")

    # --------------------------

    def delete(self):

        employee_id = input("Enter Employee ID: ")

        rows = []

        found = False

        with open(self.filename, "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

        new_rows = []

        for row in rows:

            if row[0] == employee_id:

                found = True

            else:

                new_rows.append(row)

        if not found:

            print("Employee Not Found.")

            return

        with open(self.filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(new_rows)

        print("Employee Deleted Successfully.")

    # --------------------------

    def search(self):

        keyword = input("Enter Employee Name: ").lower()

        found = False

        with open(self.filename, "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                if keyword in row[1].lower():

                    found = True

                    print("-" * 40)

                    print("ID :", row[0])

                    print("Name :", row[1])

                    print("Age :", row[2])

                    print("Department :", row[3])

                    print("Salary :", row[4])

        if not found:

            print("Employee Not Found.")

    # --------------------------

    def count(self):

        with open(self.filename, "r") as file:

            reader = csv.reader(file)

            next(reader)

            total = sum(1 for _ in reader)

        print(f"Total Employees : {total}")