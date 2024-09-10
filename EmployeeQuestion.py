class Employee:
    employee_count = 101

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.eid = "E "+ str(Employee.employee_count)
        Employee.employee_count += 1

    def show_details(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Designation: ", self.designation)
        print("Employee_Count: ", Employee.employee_count)
        print("Employee_id: ", self.eid)

    @classmethod
    def total_employee(cls):
        return cls.employee_count-101

e= Employee("Arbaz",23000,"B2B")
e.show_details()
print(e.total_employee())
print()
f= Employee("XYZ", 20000, "B2C")
f.show_details()
print(f.total_employee())