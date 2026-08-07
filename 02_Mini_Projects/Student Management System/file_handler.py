import json
from student import Student


def save_students(students):

    data = []

    for student in students:

        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "class": student.student_class,
            "marks": student.marks
        })

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)


def load_students():

    students = []

    try:

        with open("students.json", "r") as file:

            data = json.load(file)

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

        pass

    return students

















































# import json

# def save_students(students):

#     data = []

#     for student in students:

#         data.append({
#             "id": student.id,
#             "name": student.name,
#             "age": student.age,
#             "class": student.student_class,
#             "marks": student.marks
#         })

#     with open("students.json", "w") as file:
#         json.dump(data, file, indent=4)


# def load_students():

#     try:

#         with open("students.json", "r") as file:

#             return json.load(file)

#     except FileNotFoundError:

#         return []