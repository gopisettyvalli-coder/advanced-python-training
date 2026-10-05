import csv
import json
import os

from models.employee import Employee

from config.settings import (
    JSON_FILE,
    CSV_FILE
)


class EmployeeStorage:

    def __init__(self):

        self.json_file = JSON_FILE
        self.csv_file = CSV_FILE

        self.create_directories()

    def create_directories(self):

        json_folder = os.path.dirname(self.json_file)
        csv_folder = os.path.dirname(self.csv_file)

        if json_folder:
            os.makedirs(
                json_folder,
                exist_ok=True
            )

        if csv_folder:
            os.makedirs(
                csv_folder,
                exist_ok=True
            )

    # ---------------- JSON SAVE ----------------

    def save_json(self, employees):

        data = []

        for employee in employees:
            data.append(employee.to_dict())

        with open(
            self.json_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # ---------------- JSON LOAD ----------------

    def load_json(self):

        if not os.path.exists(self.json_file):
            return []

        try:

            with open(
                self.json_file,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            employees = []

            for item in data:

                employee = Employee.from_dict(item)

                employees.append(employee)

            return employees

        except (
            json.JSONDecodeError,
            KeyError,
            TypeError
        ):

            return []

    # ---------------- CSV EXPORT ----------------

    def export_csv(self, employees):

        with open(
            self.csv_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            fieldnames = [
                "employee_id",
                "name",
                "age",
                "email",
                "salary",
                "department",
                "skills"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for employee in employees:

                data = employee.to_dict()

                data["skills"] = ", ".join(
                    employee.skills
                )

                writer.writerow(data)