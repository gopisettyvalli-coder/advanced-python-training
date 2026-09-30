import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="company_db",
        user="postgres",
        password="your_password"
    )

    print("Connected successfully")

except psycopg2.Error as error:
    print("Database error:", error)

finally:
    if 'connection' in locals():
        connection.close()