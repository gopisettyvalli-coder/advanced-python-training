import csv

with open("sample.csv", "r")as file:
    data= csv.reader(file)

    for row in data:
        print(row)