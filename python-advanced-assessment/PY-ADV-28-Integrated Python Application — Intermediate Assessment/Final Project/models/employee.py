class Person:

    def __init__(self, name):
        self.name = name

class Employee(Person):

    def __init__(
        self,
        employee_id,
        name,
        age,
        email,
        salary,
        department,
        skills
    ):
        super().__init__(name)

        self.employee_id = employee_id
        self.age = age
        self.email = email
        self.salary = salary
        self.department = department
        self.skills = skills

    def to_dict(self):

        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "salary": self.salary,
            "department": self.department,
            "skills": self.skills
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            data["employee_id"],
            data["name"],
            data["age"],
            data["email"],
            data["salary"],
            data["department"],
            data["skills"]
        )

    def display(self):

        print("\n-----------------------------")
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Email       :", self.email)
        print("Salary      :", self.salary)
        print("Department  :", self.department)
        print("Skills      :", ", ".join(self.skills))
        print("-----------------------------")