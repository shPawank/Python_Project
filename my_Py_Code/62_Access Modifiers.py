#Access Modifiers in Python
#Punlic Private and Protected
#Public: can be accessed from anywhere
#Private: can only be accessed within the class
#Protected: can be accessed within the class and its subclasses

class Employee:
    def __init__(self):
        self.name = "Harry"

a=Employee()  
print(a.name)   #Public



#Private example
class Employee1:
    def __init__(self):
        self.__name = "Harry Potter"   #Private variable
e=Employee1()
#print(e.__name)   #Private variable cannot be accessed outside the class
print(e._Employee1__name)   #Private variable can be accessed using name mangling #can be accessed using _classname__variablename/idirectly

#print(a.__dir__())   #to see all the attributes of the class

#Protected example
print("\nProtected example\n")
class Student:
    def __init__(self):
        self._name = "Hermione"   #Protected variable

    def _funname(self):
        return "Hermi" 
class subject(Student):
    def show(self):
        pass
obj=subject()
obj1=Student()

print(obj._name)   #Protected variable can be accessed outside the class but it is not recommended
print(obj._funname())   #Protected method can be accessed outside the class but it is not recommended

print(obj1._name)   #Protected variable can be accessed outside the class but it is not recommended
print(obj1._funname())   #Protected method can be accessed outside the class but it is not recommended
