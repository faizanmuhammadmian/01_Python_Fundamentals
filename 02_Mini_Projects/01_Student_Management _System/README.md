#  Student Management System

A simple and efficient **Student Management System** developed in **Python** to demonstrate core programming concepts such as Object-Oriented Programming (OOP), file handling, exception handling, modular programming, and data management.

The application provides a command-line interface (CLI) that allows users to manage student records efficiently through common CRUD (Create, Read, Update, Delete) operations while storing data persistently using JSON.

---

#  Overview

Managing student records is one of the most common real-world programming problems. This project provides a practical implementation of a student management system where users can add, search, update, view, and delete student information.

The project emphasizes clean code organization, reusable components, and Python best practices, making it suitable for beginners who want to strengthen their programming fundamentals.

---

#  Features

- Add new student records
- View all students
- Search students by ID
- Update existing student information
- Delete student records
- Prevent duplicate student IDs
- Input validation using exception handling
- Persistent data storage using JSON
- Modular project structure
- Object-Oriented Programming (OOP) implementation
- User-friendly command-line interface

---

#  Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Exception Handling
- Modular Programming

---

# Architecture of my Code:
Student Management System

```
── Create Empty Student List
│
├── Define All Functions
│     │
│     ├── add_student()
│     ├── view_students()
│     ├── search_student()
│     ├── update_student()
│     └── delete_student()
│
├── Start Main Loop (while True)
│     │
│     ├── Display Menu
│     ├── Read User Choice
│     ├── Execute Function
│     └── Repeat
│
└── Exit Program
```
---

#  Project Structure

The project structure is currently organized as a modular, multi-file structure. This approach will make it easier to update, improve, maintain, organize, and scale the codebase in the future.

```
Student_Management_System/
│
├── main.py                 # Application entry point
├── student.py              # Student class
├── student_manager.py      # Student management logic
├── utils.py                # Utility functions
├── students.json           # Student database
├── README.md
├── LICENSE
└── .gitignore
```
---
# Final Architecture
```

                 main.py
                    │
                    ▼
          student_manager.py
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
 student.py                  students.json
      │
      ▼
 Student Object
      │
      ▼
 display()
 update_marks()
 to_dict()

                    ▲
                    │
                utils.py
```
---
# 🏗 Project Architecture

```
          User
            │
            ▼
       Command Line Interface
            │
            ▼
          main.py
            │
     ┌──────┼────────┐
     ▼      ▼        ▼
student.py utils.py student_manager.py
            │
            ▼
      students.json
```

---

#  Concepts Demonstrated

This project demonstrates the practical application of:

- Variables
- Data Types
- Conditional Statements
- Loops
- Functions
- Object-Oriented Programming (OOP)
- Exception Handling
- File Handling
- JSON
- Modules
- Modular Programming

---

#  Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Student_Management_System.git
```

---

## 2. Navigate to the Project

```bash
cd Student_Management_System
```

---

## 3. Run the Application

```bash
python main.py
```

---

#  Data Storage

Student information is stored in a JSON file (`students.json`), allowing records to persist even after the application is closed.

Example:

```json
[
    {
        "id": 101,
        "name": "Ali",
        "age": 20,
        "class": "BSCS",
        "marks": 92
    }
]
```

---

#  Learning Objectives

This project focuses on:

- Designing modular Python applications
- Working with classes and objects
- Implementing CRUD operations
- Reading and writing JSON files
- Handling runtime exceptions
- Organizing projects using multiple modules
- Writing clean and maintainable code

---

#  Future Improvements

Possible future enhancements include:

- Graphical User Interface (GUI)
- Database integration (SQLite/MySQL)
- Student attendance management
- Grade calculation
- Search by multiple fields
- Export records to CSV or Excel
- User authentication
- Logging system

---

#  Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to improve this project, feel free to fork the repository and submit a pull request.

---

#  License

This project is licensed under the MIT License.

---

#  Author

**Mian Muhammad Faizan**

Computer Science Student

GitHub:
https://github.com/faizanmuhammadmian

LinkedIn:
https://www.linkedin.com/in/mian-muhammad-faizan

---

 If you found this project useful, consider giving it a star.