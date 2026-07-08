#Inheritance in Python 

# class employee:
#     def __init__(self, name, id):
#         self.name=name
#         self.id=id

#     def showDetails(self):
#         print(f"Name is {self.name} and ID is {self.id}")


# class programmer(employee):
#     def showlanguage(self):
#         print("Python is the best language")

# e=employee("John", 101)
# e.showDetails()
# e1=employee("Doe", 102)
# e1.showDetails()

# e3=programmer("Smith", 103)
# e3.showDetails()
# e3.showlanguage()





class manager():
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def showDetails(self):
        print(f"Name is {self.name} and Salary is {self.salary}")

class employee(manager):
    def showlanguage(self):
        print("Java is the best language")


class intern(employee):
    def showlanguage(self):
        print("C is the best language")



m=manager("John", 10000)
m.showDetails()

e=employee("Doe", 20000)
e.showDetails()
e.showlanguage()

i=intern("Smith", 5000)
i.showDetails() 
i.showlanguage()
