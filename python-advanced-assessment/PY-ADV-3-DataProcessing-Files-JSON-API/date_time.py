# Display current time
from datetime import datetime
now = datetime.now()
print("Current date and time:", now)

# Display only date
today = datetime.now()
print("Date:", today.date())

# Display date in specific format
today = datetime.now()
formatted_date = today.strftime("%d-%m-%Y")
print("Date:", formatted_date)

# Calaculate age
birth_year = 2004
current_year = datetime.now().year
age = current_year - birth_year
print("Age:", age)