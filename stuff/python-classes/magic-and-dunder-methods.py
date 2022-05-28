class Employee:
    # default raise amount:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first.lower(), last.lower())
        self.fullname = '{} {}'.format(first, last)
    
    # custom initialization method:
    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split(sep="-")
        return cls(first=first, last=last, pay=pay)
    
    # dunder __repr__ method:
    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    # dunder __str__ method:
    def __str__(self) -> str:
        return "{} - {}".format(self.fullname, self.email)
        pass

    # add two employees together:
    def __add__(self, other):
        return self.pay + other.pay
    
    # dunder __len__():
    def __len__(self):
        return len(self.fullname)




emp1 = Employee(first="mwavu", last="kennedy", pay=20000)
emp2 = Employee(first="Jacob", last="William", pay=50000)
emp3 = Employee.from_string(string="caleb-kimutai-100000")
# print(emp2.email)
# print(emp1.fullname)
# print(emp3.email)

class Developer(Employee):
    # change raise amount for developers:
    raise_amount = 1.1

    # add arg `language` to init method:
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language
    
    # customize `from_string` method:
    @classmethod
    def from_string(cls, string):
        first, last, pay, language = string.split(sep="-")
        return cls(first, last, pay, language)


dev1 = Developer(first="joy", last="Mbuguga", pay=70000, language="JavaScript")
dev2 = Developer(first="joshua", last="Mwangangi", pay = 200000, language="python")
dev3 = Developer.from_string("eston-kagwima-20000-R")
# print(dev3.fullname)
# print(dev3.language)
# print(dev2.fullname)
# print(dev1.language)

# print(dev1)
# print(dev2)

# print(repr(emp1))
# print(repr(dev3))

# 1 + 1 basically calls int's dunder __add__() method:
# print(int.__add__(1, 1))
# print(str.__add__("a", "b"))

# add salaries of emp1 and emp2:
# print(emp1.__add__(emp2))
# print(emp1 + emp2)

# get length of employee's fullname:
print(dev1.fullname)
print(dev1.__len__())
print(len(dev1))