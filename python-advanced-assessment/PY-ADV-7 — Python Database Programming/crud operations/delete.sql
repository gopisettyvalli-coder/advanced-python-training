cursor.execute(
    "DELETE FROM employee WHERE employee_id = %s",
    (104,)
)

connection.commit()