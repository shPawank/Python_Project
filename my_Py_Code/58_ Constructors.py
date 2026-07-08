#Constructors in Python

class person():

    def __init__(self,n,o):
        print("Constructor is called")
        self.name=n
        self.occupation=o

    def info(self):
        print(f"Name: {self.name} is a {self.occupation}")

p1=person("Pawan","Data Scientist")
p2=person("Priya","Software Engineer")
p3=person(1,2,3)

p1.name="Rahul"
p1.occupation="Data Scientist"

p2.name="Priya"
p2.occupation="Software Engineer"



p1.info()
p2.info()