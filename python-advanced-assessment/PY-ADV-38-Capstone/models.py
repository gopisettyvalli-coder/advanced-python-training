from abc import ABC
from validators import validate_employee

class Employee(ABC):
    def __init__(self, emp_id, name, age, email):
        validate_employee(emp_id, name, age, email)

        self._emp_id = emp_id
        self._name = name.strip()
        self._age = age
        self._email = email.strip()

    @property
    def emp_id(self):
        return self._emp_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def email(self):
        return self._email

    def display_details(self):
        return (
            f"ID: {self.emp_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Email: {self.email}"
        )

class Developer(Employee):
    def __init__(self, emp_id, name, age, email, programming_language):
        super().__init__(emp_id, name, age, email)
        self.programming_language = programming_language

class Manager(Employee):
    def __init__(self, emp_id, name, age, email, team_size):
        super().__init__(emp_id, name, age, email)
        self.team_size = team_size