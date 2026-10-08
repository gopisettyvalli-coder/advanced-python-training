from typing import Union

def get_employee(employee_id: Union[str, int]):
    print(employee_id)

get_employee(101)
get_employee("EMP101")


# Other example
from typing import Union
def display(value: Union[str, int]):
    print(value)

display(101)
display("Seetha")