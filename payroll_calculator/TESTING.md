# TESTING.md

## Payroll Calculator Challenge 1: Testing Instructions

This document explains how to run the automated tests for the Payroll Calculator (Challenge 1) using `pytest`.

### Prerequisites
- Python 3.8 or higher installed
- `pytest` package installed (install with `pip install pytest`)
- All dependencies for the payroll calculator project installed and importable

### Test File Location
The test file for Challenge 1 is located at:

```
payroll_calculator/tests/test_payroll_challenge1.py
```

### How to Run the Tests
1. Open a terminal and navigate to the root of your project workspace.
2. Run the following command:

```
pytest payroll_calculator/tests/test_payroll_challenge1.py
```

- This will execute all tests for Challenge 1 and display a summary of results.
- You can also run all tests in the project by simply running:

```
pytest
```

### Test Coverage
The test suite covers:
- Full-time, part-time, and contractor employees
- All tax brackets
- All deduction scenarios (health insurance, retirement, union dues)
- Edge cases: zero/negative hours, invalid employee types, salary boundaries

### Adding More Tests
- Add new test functions to `test_payroll_challenge1.py`.
- Use descriptive docstrings and comments for each test.

### Troubleshooting
- Ensure your Python environment is activated and all dependencies are installed.
- If you encounter import errors, check your `PYTHONPATH` or run from the project root.
- For more verbose output, use:

```
pytest -v payroll_calculator/tests/test_payroll_challenge1.py
```

---

For any issues, consult the README.md or contact the project maintainer.
