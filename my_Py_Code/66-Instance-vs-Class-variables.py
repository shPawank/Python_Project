# Instance variables vs Class variables in Python
# Instance variables are variables that are specific to an instance of a class. 
# They are defined within the __init__ method and are accessed using the self keyword. 
# Each instance of the class has its own copy of the instance variables.  

# Class variables are variables that are shared among all instances of a class. 
# They are defined outside of any method in the class and are accessed using the class name.

class Employee:
    companyName="ABC Corp"  # Class variable
    no_of_employees = 0  # Class variable
    def __init__(self, name):
        self.name = name  # Instance variable
        self.raise_amount = 1.05  # Class variable
        Employee.no_of_employees += 1  # Incrementing the class variable for each instance created

    def showDetails(self):
        print(f"Employee Name: {self.name} and raise amount in {self.companyName} sized {self.no_of_employees} is {self.raise_amount}")

# Employee.showDetails(emp1)  # Output: Employee Name: Alice

emp1 = Employee("Alice")
emp1.raise_amount = 1.10  # Modifying the instance variable for emp1
emp1.companyName = "XYZ Corp"  # Modifying the class variable for emp1
Employee.companyName = "WXYCorp"  # Modifying the class variable for all instances
print(Employee.companyName)  # Output: WXYCorp
emp1.showDetails()  # Output: Employee Name: Alice



emp2 = Employee("Bob")
emp2.companyName = "Meta"  # Modifying the class variable for emp2
emp2.showDetails()  # Output: Employee Name: Bob

