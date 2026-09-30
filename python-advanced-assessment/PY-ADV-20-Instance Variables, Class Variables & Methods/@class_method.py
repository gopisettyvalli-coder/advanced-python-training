class Student:
    college="ABC College"

    @classmethod
    def display_college(cls):
        print(cls.college)

Student.display_college()

print("===============================================")

# changing class variable

class Employee:
    company="ABC"

    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company

print(Employee.company)
Employee.change_company("Blackroth")
print(Employee.company) 






    