SELECT
    employee.employee_id,
    employee.name,
    department.department_name
FROM employee
JOIN department
ON employee.department_id = department.department_id;