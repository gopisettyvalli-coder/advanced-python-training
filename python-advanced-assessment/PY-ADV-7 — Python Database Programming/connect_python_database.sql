import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="company_db",
    user="postgres",
    password="your_password"
)

print("Database connected successfully")

connection.close()