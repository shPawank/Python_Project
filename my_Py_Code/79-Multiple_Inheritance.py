#Multiple Inheritance in Python
#Multiple inheritance is a feature in object-oriented programming where a class can inherit attributes and methods from more than one parent class. 
#This allows a subclass to combine the functionality of multiple classes, enabling code reuse and creating more complex class hierarchies.   

class Employee:
    def __init__(self, name):
        self.name=name

    def show(self):
        return f"Employee Name: {self.name}"

class Dancer:
    def __init__(self, style):
        self.style=style

    def show(self):
        return f"Dancer Style: {self.style}"

class DancerEmployee(Employee, Dancer):
    def __init__(self, name, style):
        self.name=name
        self.style=style


d=DancerEmployee("Pawan", "Hip Hop")
print(d.show())  # Output: Employee Name: Pawan

print(d.style)  # Output: Hip Hop

o=Dancer("Ballet")
print(o.show())  # Output: Dancer Style: Ballet

print(DancerEmployee.__mro__)  # Output: (<class '__main__.DancerEmployee'>, <class '__main__.Employee'>, <class '__main__.Dancer'>, <class 'object'>)
print(DancerEmployee.mro())
    