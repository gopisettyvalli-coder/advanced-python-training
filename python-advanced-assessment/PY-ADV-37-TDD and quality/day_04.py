import pytest
from unittest.mock import Mock

# Custom Exception
class InvalidEmployeeError(Exception):
    pass

# Employee Class
class Employee:
    def __init__(self, emp_id, name, age, email):
        if emp_id <= 0:
            raise InvalidEmployeeError("Employee ID must be positive")

        if not name:
            raise InvalidEmployeeError("Name cannot be empty")

        if age < 18:
            raise InvalidEmployeeError("Employee must be at least 18")

        if "@" not in email:
            raise InvalidEmployeeError("Invalid email address")

        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email

# Employee Storage
class EmployeeStorage:
    def __init__(self):
        self.employees = {}

    def add(self, employee):
        self.employees[employee.emp_id] = employee

    def get(self, emp_id):
        return self.employees.get(emp_id)

# Employee Service
class EmployeeService:
    def __init__(self, storage):
        self.storage = storage

    def add_employee(self, employee):
        self.storage.add(employee)
        return "Employee added successfully"

    def get_employee(self, emp_id):
        return self.storage.get(emp_id)

@pytest.fixture
def employee():
    return Employee(
        101,
        "Seetha",
        25,
        "seetha@gmail.com"
    )

@pytest.fixture
def storage():
    return EmployeeStorage()

@pytest.fixture
def service(storage):
    return EmployeeService(storage)

# Test valid employee creation
def test_create_employee(employee):
    assert employee.emp_id == 101
    assert employee.name == "Seetha"
    assert employee.age == 25

# Parameterized validation tests
@pytest.mark.parametrize(
    "emp_id, name, age, email",
    [
        (0, "Seetha", 25, "seetha@gmail.com"),
        (101, "", 25, "seetha@gmail.com"),
        (101, "Seetha", 17, "seetha@gmail.com"),
        (101, "Seetha", 25, "invalid-email"),
    ]
)
def test_invalid_employee(emp_id, name, age, email):
    with pytest.raises(InvalidEmployeeError):
        Employee(emp_id, name, age, email)

# Test adding an employee
def test_add_employee(service, employee, storage):
    result = service.add_employee(employee)

    assert result == "Employee added successfully"
    assert storage.get(101) == employee

# Test retrieving an employee
def test_get_employee(service, employee):
    service.add_employee(employee)
    result = service.get_employee(101)
    assert result.name == "Seetha"

# Test retrieving a nonexistent employee
def test_employee_not_found(service):
    assert service.get_employee(999) is None

# Test mocking storage
def test_service_with_mock(employee):
    mock_storage = Mock()
    service = EmployeeService(mock_storage)
    service.add_employee(employee)
    mock_storage.add.assert_called_once_with(employee)