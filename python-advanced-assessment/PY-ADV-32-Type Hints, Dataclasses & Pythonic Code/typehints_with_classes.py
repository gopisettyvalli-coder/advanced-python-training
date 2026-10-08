class Employee:
    def __init__(self, name:str, salary:int):
        self.name=name
        self.salary=salary

    def display(self)-> str:
        return f"{self.name} earns {self.salary}"

employee=Employee("Seetha", 80000)
print(employee.display())

