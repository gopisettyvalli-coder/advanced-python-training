import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="company_db",
        user="postgres",
        password="your_password"
    )