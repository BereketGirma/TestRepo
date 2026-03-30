from models.employee_type import Employee_Type
from models.employee import Employee
from models.pay_slip import Pay_Slip

class Payroll_Processor:
    # Deducations
    HEALTH_INSURANCE = 150
    UNION_DUES = 50
    RETIREMENT = 0.05

    MAX_PART_TIME_HOURS = 120

    @staticmethod
    def round_currency(value: int) -> int:
        """
        Rounds the value passed into two decimal points.
        
        :param value: The currency that is being rounded
        """
        return round(value, 2)

    def calculate_gross_pay(self, employee: Employee, hours_or_days=0) -> None | int:
        """
        Calculates the gross pay for provided employee
        
        :param employee: Object that reference to the employee
        :param hours_or_days: Worked hours/days
        """
        if hours_or_days < 0:
            raise ValueError("Hours or days worked cannot be negative.")
        
        if employee.employee_type == Employee_Type.FULL_TIME:
            gross = employee.pay_rate
        elif employee.employee_type == Employee_Type.PART_TIME:
            hours = min(hours_or_days, self.MAX_PART_TIME_HOURS)
            gross = employee.pay_rate * hours
        elif employee.employee_type == Employee_Type.CONTRACTOR:
            gross = employee.pay_rate * hours_or_days
        else:
            raise ValueError("Unknown employee type provided")

        return self.round_currency(gross)

    def calculate_tax(self, gross_pay: int) -> int:
        """
        Calculates tax based on the following tax bracket:

        0-1000$ -> 0%\n
        1001-3000$ -> 10%\n
        3001-5000$ -> 20%\n
        over 5000$ -> 30%\n
        
        :param gross_pay: The reference pay used to calculate tax
        """
        if gross_pay <= 1000:
            rate = 0.0
        elif gross_pay <= 3000:
            rate = 0.10
        elif gross_pay <= 5000:
            rate = 0.20
        else:
            rate = 0.30
        
        return self.round_currency(gross_pay * rate)

    def calculate_deductions(self, employee: Employee, gross_pay: int) -> dict:
        """
        Applies any pluasible deductions to the employees pay
        
        :param employee: Object that reference to the employee
        :type employee: Employee
        :param gross_pay: The amount for the employee pay
        :type gross_pay: int
        :return: All deductions of the employees pay 
        :rtype: dict
        """
        deductions = {}
        
        if employee.employee_type == Employee_Type.FULL_TIME:
            deductions["health_insurance"] = self.HEALTH_INSURANCE
        
        if employee.has_retirement:
            deductions["retirement"] = self.round_currency(gross_pay * self.RETIREMENT)

        if employee.is_union_member:
            deductions["union_dues"] = self.UNION_DUES
        
        return deductions

    def generate_pay_slip(self, employee: Employee, hours_or_days=0) -> Pay_Slip:
        """
        Gathers all information and creates a pay slip
        
        :param employee: Object that reference to the employee
        :type employee: Employee
        :param hours_or_days: Number of hours or days worked by employee
        :return: Pay slip object containing all detials about the pay
        :rtype: Pay_Slip
        """
        gross = self.calculate_gross_pay(employee, hours_or_days)
        tax = self.calculate_tax(gross)
        deductions = self.calculate_deductions(employee, gross)

        total_deducations = sum(deductions.values())
        net = self.round_currency(gross - tax - total_deducations)

        return Pay_Slip(employee, gross, tax, deductions, net)

    def process_monthly_payroll(self, employee_list, work_data) -> list:
        """
        Processes the monthly payroll for a list of employees
        
        :param employee_list: List of objects that reference to a single employee
        :param work_data: dict mapping employee id to hours or days worked
        :return: Returns back a list of all pay slips of the employees
        :rtype: list
        """
        pay_slips = []

        for employee in employee_list:
            hours_or_days = work_data.get(employee.id, 0)
            slip = self.generate_pay_slip(employee, hours_or_days)
            pay_slips.append(slip)

        return pay_slips        