# person.py
"""The person class for use in the classroom app"""

import datetime

class Person:
    """Person class"""
    def __init__(self,
                 first_name:str,
                 last_name:str,
                 date_of_birth:datetime.date,
                 preferred_name:str=None,
                 image_path:str=None) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.preferred_name = preferred_name or first_name
        self.image_path = image_path or "images/blank.jpg"
        self.date_of_birth = date_of_birth
        self.age = (datetime.date.today() - self.date_of_birth).days // 365.25

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
