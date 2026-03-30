from services.payroll_processor import Payroll_Processor
from models.employee import Employee
from models.employee_type import Employee_Type

if __name__ == "__main__":
    processor = Payroll_Processor()

    employees = [
        Employee(1, "Alice", Employee_Type.FULL_TIME, 4000, True, True),
        Employee(2, "Bob", Employee_Type.FULL_TIME, 2500, False, False),
        Employee(3, "Charlie", Employee_Type.PART_TIME, 20, True, True),
        Employee(4, "Dave", Employee_Type.PART_TIME, 25, False, True),
        Employee(5, "Eve", Employee_Type.CONTRACTOR, 300, True, True),
        Employee(6, "Frank", Employee_Type.CONTRACTOR, 200, False, False),
    ]

    work_data = {
        3: 100,
        4: 130,
        5: 15,
        6: 10,
    }

    slips = processor.process_monthly_payroll(employees, work_data)

    for slip in slips:
        print(slip)