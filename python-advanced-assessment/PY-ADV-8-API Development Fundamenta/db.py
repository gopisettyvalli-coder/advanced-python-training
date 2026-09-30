import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="student_db",
        user="postgres",
        password="Valli12"
    )

    return connection