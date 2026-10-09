from dataclasses import dataclass

@dataclass
class Employee:
    employee_id: int
    name: str
    department: str
    salary: float
    experience: int

    def __post_init__(self):
        if self.employee_id <= 0:
            raise ValueError("Employee ID must be positive")

        if not self.name.strip():
            raise ValueError("Employee name cannot be empty")

        if self.salary < 0:
            raise ValueError("Salary cannot be negative")

        if self.experience < 0:
            raise ValueError("Experience cannot be negative")

    def calculate_bonus(self) -> float:
        if self.experience >= 5:
            return self.salary * 0.10
        return self.salary * 0.05

    def calculate_total_salary(self) -> float:
        return self.salary + self.calculate_bonus()