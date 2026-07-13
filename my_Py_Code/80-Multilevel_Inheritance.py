#Multilevel Inheritance in Python
#Multilevel inheritance is a feature in object-oriented programming where a class can inherit from another class, which in turn inherits from another class.
#This creates a chain of inheritance, where a subclass can inherit properties and methods from its parent class, and that parent class can inherit

class Grandfather:
    def __init__(self, name):
        self.name=name

    def show(self):
        return f"Grandfather Name: {self.name}"

class Father(Grandfather):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of the parent class
        self.age=age

    def show(self):
        return f"Father Name: {self.name}, Age: {self.age}"

class Son(Father):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.hobby=hobby

    def show(self):
        return (f"{Grandfather.show(self)}\n"
                f"{Father.show(self)}\n"
                f"Son Name: {self.name}, Hobby: {self.hobby}")



g=Grandfather("John")
f=Father("Jane", 40)
s=Son("Bob", 15, "Reading")
 
# print(g.show())
# print(f.show())
print(s.show()) 