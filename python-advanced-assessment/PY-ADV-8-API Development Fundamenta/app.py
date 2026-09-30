from flask import Flask, jsonify
import psycopg2
app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="localpostgres",
        database="student_db",
        user="postgres",
        password="Valli12",
        port="5432"
    )

@app.route("/students", methods=["GET"])
def get_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    students = []

    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "course": row[3]
        })

    cursor.close()
    connection.close()

    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=True)