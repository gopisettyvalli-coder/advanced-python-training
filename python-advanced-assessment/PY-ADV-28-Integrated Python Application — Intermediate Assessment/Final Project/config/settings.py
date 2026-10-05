import os
from dotenv import load_dotenv
load_dotenv()


APP_NAME = os.getenv(
    "APP_NAME",
    "Employee Management System"
)

JSON_FILE = os.getenv(
    "JSON_FILE",
    "data/employees.json"
)

CSV_FILE = os.getenv(
    "CSV_FILE",
    "data/employees.csv"
)

LOG_FILE = os.getenv(
    "LOG_FILE",
    "logs/application.log"
)