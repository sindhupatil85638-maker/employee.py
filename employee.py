def employee_details(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )

# Get employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
salary = input("Enter Salary: ")

print("\nEmployee Details:")
print(employee_details(name, emp_id, department, salary))
