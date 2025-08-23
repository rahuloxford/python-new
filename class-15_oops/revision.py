
class Employee:
    def __init__(self, empId, firstName, lastName, salary):
        self.empId= empId
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def emp_details(self):
        return f"Employee Id: {self.empId} \nEmployee Name: {self.firstName} {self.lastName}"


emp1 = Employee(103, "Tom", "Odell", 45000)
emp2 = Employee(107, "Chris", "Evans", 85000)

print(emp1.emp_details())
print(emp2.emp_details())