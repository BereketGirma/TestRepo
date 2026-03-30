from models.employee_type import Employee_Type
class Employee:
    def __init__(self, id, name, employee_type, pay_rate, is_union_member=False, has_retirement=False):
        if pay_rate < 0:
            raise ValueError("Pay rate cannot be negative.")
        
        if not isinstance(employee_type, Employee_Type):
            raise ValueError("Invalid employee type provided.")

        self.id = id
        self.name = name
        self.employee_type = employee_type
        self.pay_rate = pay_rate
        self.is_union_member = is_union_member
        self.has_retirement = has_retirement