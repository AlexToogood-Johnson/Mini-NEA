# classroom.py
"""The classroom class for the Mini-NEA project"""

from person import Person

class Classroom:
    """Classroom class"""
    def __init__(self, teacher:Person, class_name:str, students:list) -> None:
        self.teacher = teacher
        self.class_name = class_name
        self.students = students

    def add_student(self, student:Person) -> None:
        """Adds a student to the class"""
        self.students.appemd(student)

    def remove_student(self, student:Person) -> None:
        """Removes a student from the class"""
        self.students.remove(student)
