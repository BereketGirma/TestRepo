"""
Test suite for Challenge 1: Payroll Calculator
Uses pytest to validate payroll calculations and edge cases.
"""
import pytest
from services.payroll_processor import Payroll_Processor
from models.employee import Employee
from models.employee_type import Employee_Type

# Helper for readable slip output
from models.pay_slip import Pay_Slip

def slip_to_dict(slip):
    return {
        'employee': slip.employee.name,
        'gross_pay': slip.gross_pay,
        'tax': slip.tax_amount,
        'deductions': slip.deductions_map,
        'net_pay': slip.net_pay,
    }

def test_full_time_all_benefits():
    """Test full-time employee with all benefits and high salary (edge: max deductions, 20% tax bracket)."""
    emp = Employee(1, "Alice", Employee_Type.FULL_TIME, 4000, True, True)
    proc = Payroll_Processor()
    slip = proc.generate_pay_slip(emp)
    expected = {
        'employee': 'Alice',
        'gross_pay': 4000,
        'tax': 800,  # 20%
        'deductions': {'health_insurance': 150, 'retirement': 200.0, 'union_dues': 50},
        'net_pay': 4000 - 800 - 150 - 200 - 50
    }
    assert slip_to_dict(slip) == expected

def test_full_time_no_benefits_low_salary():
    """Test full-time employee with no benefits and low salary (edge: 0% tax bracket, no deductions)."""
    emp = Employee(2, "Bob", Employee_Type.FULL_TIME, 900, False, False)
    proc = Payroll_Processor()
    slip = proc.generate_pay_slip(emp)
    expected = {
        'employee': 'Bob',
        'gross_pay': 900,
        'tax': 0,  # 0%
        'deductions': {'health_insurance': 150},
        'net_pay': 750
    }
    assert slip_to_dict(slip) == expected

def test_part_time_max_hours():
    """Test part-time employee with hours above max allowed (edge: hours capped at 120)."""
    emp = Employee(3, "Charlie", Employee_Type.PART_TIME, 20, True, True)
    proc = Payroll_Processor()
    slip = proc.generate_pay_slip(emp, hours_or_days=200)
    expected_gross = 20 * 120  # capped at 120
    expected_tax = proc.calculate_tax(expected_gross)
    expected_deductions = {'retirement': round(expected_gross * 0.05, 2), 'union_dues': 50}
    expected_net = expected_gross - expected_tax - sum(expected_deductions.values())
    assert slip_to_dict(slip) == {
        'employee': 'Charlie',
        'gross_pay': expected_gross,
        'tax': expected_tax,
        'deductions': expected_deductions,
        'net_pay': round(expected_net, 2)
    }

def test_part_time_zero_hours():
    """Test part-time employee with zero hours (edge: no pay, no deductions, no tax)."""
    emp = Employee(4, "Dave", Employee_Type.PART_TIME, 25, False, False)
    proc = Payroll_Processor()
    slip = proc.generate_pay_slip(emp, hours_or_days=0)
    assert slip_to_dict(slip) == {
        'employee': 'Dave',
        'gross_pay': 0,
        'tax': 0,
        'deductions': {},
        'net_pay': 0
    }

def test_contractor_typical():
    """Test contractor with typical days worked (edge: no deductions, tax bracket check)."""
    emp = Employee(5, "Eve", Employee_Type.CONTRACTOR, 300, False, False)
    proc = Payroll_Processor()
    slip = proc.generate_pay_slip(emp, hours_or_days=10)
    gross = 300 * 10
    tax = proc.calculate_tax(gross)
    assert slip_to_dict(slip) == {
        'employee': 'Eve',
        'gross_pay': gross,
        'tax': tax,
        'deductions': {},
        'net_pay': gross - tax
    }

def test_contractor_zero_days():
    """Test contractor with zero days worked (edge: no pay, no deductions, no tax)."""
    emp = Employee(6, "Frank", Employee_Type.CONTRACTOR, 200, False, False)
    proc = Payroll_Processor()
    slip = proc.generate_pay_slip(emp, hours_or_days=0)
    assert slip_to_dict(slip) == {
        'employee': 'Frank',
        'gross_pay': 0,
        'tax': 0,
        'deductions': {},
        'net_pay': 0
    }

def test_invalid_employee_type():
    """Test with an invalid employee type (edge: should raise ValueError)."""
    class FakeType: pass
    with pytest.raises(ValueError):
        emp = Employee(7, "Ghost", FakeType(), 1000)
        proc = Payroll_Processor()
        proc.generate_pay_slip(emp)

def test_full_time_highest_tax_bracket():
    """Test full-time employee in highest tax bracket (edge: >$5000, 30% tax)."""
    emp = Employee(8, "Richie", Employee_Type.FULL_TIME, 6000, True, True)
    proc = Payroll_Processor()
    slip = proc.generate_pay_slip(emp)
    expected_gross = 6000
    expected_tax = proc.calculate_tax(expected_gross)
    expected_deductions = {'health_insurance': 150, 'retirement': round(expected_gross * 0.05, 2), 'union_dues': 50}
    expected_net = expected_gross - expected_tax - sum(expected_deductions.values())
    assert slip_to_dict(slip) == {
        'employee': 'Richie',
        'gross_pay': expected_gross,
        'tax': expected_tax,
        'deductions': expected_deductions,
        'net_pay': round(expected_net, 2)
    }
