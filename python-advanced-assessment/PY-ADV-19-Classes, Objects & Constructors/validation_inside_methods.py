class Employee:
    def set_details(self,name,age,salary):

        if name==" ":
            print("Name cannot be empty")
            return

        if age<0:
            print("Age must be greater than 0")
            return

        if salary<0:
            print("Salary should not be negative")
            return

        self.name=name
        self.age=age
        self.salary=salary

        print("Employee details added successfully")

employee=Employee()
employee.set_details("Radha", 29, 90000)

employee.set_details("Seetha", -5, 80000)
