from employee import employee_info

def test_employee_details():
    result = employee_info("Rahul", "EMP01", "IT", "50000")

    expected = (
        "Employee Name: Rahul\n"
        "Employee ID: EMP01\n"
        "Department: IT\n"
        "Salary: 50000"
    )
  assert result == expected
