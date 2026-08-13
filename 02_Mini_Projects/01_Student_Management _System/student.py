class Student:

    def __init__(self, student_id, name, age, student_class, marks):

        self.id = student_id
        self.name = name
        self.age = age
        self.student_class = student_class
        self.marks = marks

    def display(self):

        print("-" * 30)
        print("ID    :", self.id)
        print("Name  :", self.name)
        print("Age   :", self.age)
        print("Class :", self.student_class)
        print("Marks :", self.marks)


    def update_marks(self, new_marks):

        self.marks = new_marks


    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "class": self.student_class,
            "marks": self.marks
        }    