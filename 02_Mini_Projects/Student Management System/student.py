class Student:

    def __init__(self, student_id, name, age, student_class, marks):

        self.id = student_id
        self.name = name
        self.age = age
        self.student_class = student_class
        self.marks = marks

    def display(self):

        print("-" * 30)
        print("ID:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Class:", self.student_class)
        print("Marks:", self.marks)

    def update_marks(self, new_marks):

        self.marks = new_marks

    def is_passed(self):

        if self.marks >= 50:
            print("Status: Passed")
        else:
            print("Status: Failed")





























































# class Student:

#     def __init__(self, student_id, name, age, student_class, marks):

#         self.id = student_id
#         self.name = name
#         self.age = age
#         self.student_class = student_class
#         self.marks = marks

#     def display(self):

#         print("----------------------")
#         print("ID:", self.id)
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Class:", self.student_class)
#         print("Marks:", self.marks)