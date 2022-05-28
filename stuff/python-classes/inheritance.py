class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(first, last)
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("nancy", "kyalo", 50000)
emp_2 = Employee("Britney", "Winnie", 30000)

# print(emp_1.fullname())
# print(emp_2.pay)

class Developer(Employee):
    raise_amt = 1.2

    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language

dev_1 = Developer("kennedy", "mwavu", 50000, "R")
dev_2 = Developer("eston", "kagwima", 50000, "python")

# print(dev_1.fullname())
# print(dev_2.email)

class Manager(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, dept, employees=None):
        super().__init__(first, last, pay)
        self.dept = dept
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, employee_name):
        if employee_name not in self.employees:
            self.employees.append(employee_name)
    
    def rem_employee(self, employee_name):
        if employee_name in self.employees:
            self.employees.remove(employee_name)
    
    def print_employees(self):
        for employee in self.employees:
            print("-->", employee.fullname())
    

man_1 = Manager("hump", "wanyanga", 200000, "insurance", [emp_1, emp_2])
# print(man_1.email)
# print(man_1.employees)
# man_1.print_employees()

# man_1.add_employee(dev_1)
# man_1.print_employees()

# man_1.rem_employee(dev_1)
# man_1.print_employees()

# man_1.add_employee("mwavu")
# print(man_1.employees)

# man_1.rem_employee("emp1")
# print(man_1.employees)

# man_1.print_employees()

# print(isinstance(man_1, Employee))
# print(isinstance(man_1, Manager))

# print(isinstance(man_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))