# classroom.py
"""The classroom class for the Mini-NEA project"""

from person import Person

class Classroom:
    def __init__(self, max_class_size:int, teacher:Person, class_name:str, students:list) -> None:
        self.max_class_size = max_class_size
        self.teacher = teacher
        self.class_name = class_name
        self.students = students
        if self.max_class_size < len(self.students): self.max_class_size = len(self.students)

    def add_student(self, student:Person, increase_max_class_size:bool=True) -> None:
        if len(self.students) + 1 > self.max_class_size and increase_max_class_size:
            self.students.append(student)
        else:
            self.students.append(student)
            