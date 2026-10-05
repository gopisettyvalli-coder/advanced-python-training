class EmployeeManagementError(Exception):
    pass

class EmployeeAlreadyExistsError(EmployeeManagementError):
    pass

class EmployeeNotFoundError(EmployeeManagementError):
    pass

class InvalidEmployeeError(EmployeeManagementError):
    pass