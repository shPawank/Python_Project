#Class Methods as Alternative Constructors in Python

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, int(salary))

e=Employee("Alice", 50000)
print(e.name)
print(e.salary)

string="Bob-60000"
e2=Employee(string.split("-")[0], int(string.split("-")[1]))
e2=Employee.from_string(string)
print(e2.name)
print(e2.salary)


