BEGIN;

UPDATE employee
SET salary = 45000
WHERE employee_id = 101;

UPDATE employee
SET salary = 38000
WHERE employee_id = 102;

COMMIT;