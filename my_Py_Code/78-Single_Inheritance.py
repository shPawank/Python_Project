#Single Inheritance in Python
#Single inheritance is a feature in object-oriented programming where a class (called the child or subclass) inherits properties and behaviors (methods) from another class (called the parent or superclass). 
#In single inheritance, a subclass can inherit from only one superclass.  

class Animal:
    def __init__(self, name):
        self.name=name
        self.species="Animal"

    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the parent class
        self.breed=breed

    def make_sound(self):
        return "Woof!"



d=Dog("Buddy", "Golden Retriever")
print(d.name)  # Output: Buddy

a=Animal("Generic Animal")
print(a.name)  # Output: Generic Animal
print(a.make_sound())  # Output: Some generic animal sound



#Quick Quiz: Implement a cat class by using animal class. add some mehtod specific to cat class.

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the constructor of the parent class
        self.color=color

    def make_sound(self):
        return "Meow!"

    def purr(self):
        return "Purr..."

cat=Cat("Fluffy", "Orange")
print(cat.name)  # Output: Fluffy
print(cat.color)  # Output: Orange
print(cat.make_sound())  # Output: Meow!
print(cat.purr())  # Output: Purr...
