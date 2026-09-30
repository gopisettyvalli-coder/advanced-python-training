cursor.execute(
    "UPDATE employee SET salary = %s WHERE employee_id = %s",
    (35000, 104)
)

connection.commit()