from typing import Dict, List, Optional
from models import Employee
from exceptions import InvalidEmployeeError

class EmployeeStorage:

    def __init__(self) -> None:
        self._employees: Dict[int, Employee] = {}

    def add(self, employee: Employee) -> None:
        if employee.emp_id in self._employees:
            raise InvalidEmployeeError(
                "Employee ID already exists"
            )

        self._employees[employee.emp_id] = employee

    def get(self, emp_id: int) -> Optional[Employee]:
        return self._employees.get(emp_id)

    def get_all(self) -> List[Employee]:
        return list(self._employees.values())


class EmployeeService:

    def __init__(self, storage: EmployeeStorage) -> None:
        self.storage = storage

    def add_employee(self, employee: Employee) -> str:
        self.storage.add(employee)
        return "Employee added successfully"

    def get_employee(self, emp_id: int) -> Optional[Employee]:
        return self.storage.get(emp_id)

    def get_all_employees(self) -> List[Employee]:
        return self.storage.get_all()