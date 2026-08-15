from csv_manager import CSVManager
from utils import print_menu

manager = CSVManager("employees.csv")

while True:

    print_menu()

    choice = input("Enter Choice: ")

    if choice == "1":

        manager.display()

    elif choice == "2":

        manager.add()

    elif choice == "3":

        manager.update()

    elif choice == "4":

        manager.delete()

    elif choice == "5":

        manager.search()

    elif choice == "6":

        manager.count()

    elif choice == "7":

        print("Thank You!")

        break

    else:

        print("Invalid Choice.")