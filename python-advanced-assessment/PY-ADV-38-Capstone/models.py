from abc import ABC
from validators import validate_employee

class Employee(ABC):

    def __init__(
        self,
        emp_id: int,
        name: str,
        age: int,
        email: str
    ) -> None:
        validate_employee(emp_id, name, age, email)

        self._emp_id = emp_id
        self._name = name.strip()
        self._age = age
        self._email = email.strip()

    @property
    def emp_id(self) -> int:
        return self._emp_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def email(self) -> str:
        return self._email

    def display_details(self) -> str:
        return (
            f"ID: {self.emp_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Email: {self.email}"
        )


class Developer(Employee):

    def __init__(
        self,
        emp_id: int,
        name: str,
        age: int,
        email: str,
        programming_language: str
    ) -> None:
        super().__init__(emp_id, name, age, email)

        if not isinstance(programming_language, str) or not programming_language.strip():
            raise ValueError("Programming language cannot be empty")

        self.programming_language = programming_language.strip()

class Manager(Employee):

    def __init__(
        self,
        emp_id: int,
        name: str,
        age: int,
        email: str,
        team_size: int
    ) -> None:
        super().__init__(emp_id, name, age, email)

        if (
            not isinstance(team_size, int)
            or isinstance(team_size, bool)
            or team_size < 0
        ):
            raise ValueError("Team size must be a non-negative integer")

        self.team_size = team_size