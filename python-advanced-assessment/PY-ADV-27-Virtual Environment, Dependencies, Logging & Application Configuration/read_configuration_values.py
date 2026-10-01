from dotenv import load_dotenv
import os

load_dotenv()

app_name = os.getenv("APP_NAME", "My Application")
environment = os.getenv("ENVIRONMENT", "development")

print("Application:", app_name)
print("Environment:", environment)