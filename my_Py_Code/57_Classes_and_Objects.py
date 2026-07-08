#Classes and Objects in Python

class Person:
    name="Pawan"
    occupation="IT Associate"
    net_worth=100000

    def info(self):
        print(f"Name: {self.name} is a {self.occupation} and has a net worth of {self.net_worth}")

a=Person()
b=Person()

b.name="Rahul"
b.occupation="Data Scientist"
b.net_worth=200000

a.info()
b.info()