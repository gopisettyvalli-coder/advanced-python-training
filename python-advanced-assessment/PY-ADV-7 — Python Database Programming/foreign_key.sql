ALTER TABLE employee
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id)
REFERENCES department(department_id);