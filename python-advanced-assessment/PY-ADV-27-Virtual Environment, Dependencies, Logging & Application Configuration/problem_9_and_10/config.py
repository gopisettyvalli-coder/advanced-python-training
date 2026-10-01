from dotenv import load_dotenv
import os

load_dotenv()

app_name = os.getenv("APP_NAME")
environment = os.getenv("ENVIRONMENT")
database = os.getenv("DATABASE_NAME")

print("Application:", app_name)
print("Environment:", environment)
print("Database:", database)