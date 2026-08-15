# CSV Reader System

A beginner-friendly Python CRUD project using the csv module and Object-Oriented Programming (OOP).

## Features

- View Employees
- Add Employee
- Update Employee
- Delete Employee
- Search Employee
- Count Employees

## Technologies

- Python 3
- CSV Module
- OOP
- File Handling




# CSV Reader System

A simple Python project that demonstrates CRUD (Create, Read, Update, Delete) operations using CSV files. The project is built with Object-Oriented Programming (OOP) and focuses on Python fundamentals such as file handling, modules, classes, and exception handling.

## Features

- View all employees
- Add a new employee
- Update employee information
- Delete an employee
- Search employees by name
- Count total employees
- Input validation
- Exception handling
- Menu-driven interface

## Technologies Used

- Python 3
- CSV Module
- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling



# Architecture of my Code:
For single file
```
── Create CSV Manager Object
│
├── Define CSVManager Class
│     │
│     ├── __init__()
│     │
│     ├── display()
│     ├── add()
│     ├── update()
│     ├── delete()
│     ├── search()
│     └── count()
│
├── Define Helper Functions
│     │
│     ├── print_line()
│     ├── print_menu()
│     ├── get_valid_age()
│     └── get_valid_salary()
│
├── Start Main Loop (while True)
│     │
│     ├── Display Menu
│     ├── Read User Choice
│     ├── Execute Method
│     └── Repeat
│
└── Exit Program
```

## Project Structure


```
CSV_Reader/
│
├── main.py
├── csv_manager.py
├── utils.py
├── employees.csv
└── README.md
```
Architecture of my Code in files Structure is :


```
CSV Reader System
│
├── main.py
│   ├── Create CSVManager Object
│   └── Main Menu (while True)
│
├── csv_manager.py
│   └── CSVManager Class
│       ├── __init__()
│       ├── display()
│       ├── add()
│       ├── update()
│       ├── delete()
│       ├── search()
│       └── count()
│
├── utils.py
│   ├── print_line()
│   ├── print_menu()
│   ├── get_valid_age()
│   └── get_valid_salary()
│
└── employees.csv
    └── Employee Data

```

## Learning Objectives

This project helps practice:

- Python fundamentals
- Functions and Modules
- Classes and Objects (OOP)
- CSV File Handling
- Exception Handling
- Input Validation
- CRUD Operations

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in a terminal.
3. Run the following command:

```bash
python main.py
```

## Author

**Mian Muhammad Faizan**
Computer Science Student

GitHub:
https://github.com/faizanmuhammadmian

LinkedIn:
https://www.linkedin.com/in/mian-muhammad-faizan

---

 If you found this project useful, consider giving it a star.