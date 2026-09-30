class Employee:
    def __init__(self,employee_id,name,department,salary,experience):
        self.employee_id=employee_id
        self.name=name
        self.department=department
        self.salary=salary
        self.experience=experience

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.name)
        print("Employee Department:", self.department)
        print("Employee Salary:", self.salary)
        print("Employee Experience:", self.experience)

    def calaculate_bonus(self):
        bonus=self.salary*10/100

        print("Bonus:", bonus)

    def calaculate_annual_salary(self):
        annual_salary=self.salary*12

        print("Annual Salary:", annual_salary)

    def update_salary(self,new_salary):
        self.salary=new_salary

        print("Updated Salary:", self.salary)  

employee=Employee("Seetha", 104, "Python", 80000, 3)

employee.display_details()
employee.calaculate_annual_salary()
employee.calaculate_bonus()
employee.calaculate_annual_salary()
employee.update_salary(80000)
employee.display_details()

       