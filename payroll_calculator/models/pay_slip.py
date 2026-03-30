class Pay_Slip:
    def __init__(self, employee, gross_pay, tax_amount, deductions_map, net_pay):
        self.employee = employee
        self.gross_pay = gross_pay 
        self.tax_amount = tax_amount
        self.deductions_map = deductions_map
        self.net_pay = net_pay

    def __str__(self):
        return (
            f"\n----- Pay Slip -----\n"
            f"Employee: {self.employee.name}\n"
            f"Gross Pay: {self.gross_pay:.2f}\n"
            f"Tax: {self.tax_amount:.2f}\n"
            f"Deductions: {self.deductions_map}\n"
            f"Net Pay: {self.net_pay:.2f}\n"
            f"--------------------"
        )