#super keyword in Python is used to call a method from the parent class. 
#It is commonly used in inheritance to access methods and properties of a parent class from a child class.

class ParentClass:
    def parent_method(self):
        print("This is a method from the parent class.")

class ChildClass(ParentClass):

    def parent_method(self):
        print("pawan")
        super().parent_method()  # Calling the parent method using super()
     
    def child_method(self):
        print("This is a method from the child class.")
        super().parent_method()  # Calling the parent method using super()

child = ChildClass()
child.child_method()  # Output: This is a method from the child class. This is
child.parent_method()  # Output: This is a method from the parent class.







class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id


class Programmer(employee):
    def __init__(self,name, id, lang):
        # self.name=name
        # self.id=id
        super().__init__(name,id)
        self.lang=lang

rohan=employee("rohan", 101)
harry=Programmer("harry", 102, "python")


print(rohan.name)
print(harry.id)
print(harry.lang)