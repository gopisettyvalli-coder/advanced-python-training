import csv 

with open("sample.csv", "w", newline="")as file:
    writer=csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Radha", "22", "Python"])
    writer.writerow(["Rahul", "25", "Java"])
