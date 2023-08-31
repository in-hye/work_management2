class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name


class EmployeeDatabase:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, emp_name):
        if emp_id not in self.employees:
            self.employees[emp_id] = Employee(emp_id, emp_name)

    def get_employee(self, emp_id):
        return self.employees.get(emp_id)


if __name__ == "__main__":
    emp_db = EmployeeDatabase()

    emp_db.add_employee("E001", "Alice")
    emp_db.add_employee("E002", "Bob")

    emp = emp_db.get_employee("E001")
    if emp:
        print(f"Employee ID: {emp.emp_id}, Name: {emp.emp_name}")
