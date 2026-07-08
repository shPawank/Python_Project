#Decorators in Python are a powerful tool that allows you to modify the behavior of a function or class. 
# They are often used to add functionality to existing code without modifying the original code. 
# A decorator is a function that takes another function as an argument and returns a new function that can 
# be used in place of the original function.




def greeting(func):
    def mfunc(*args, **kwargs):
        print("Welcome to Python Decorators")
        func(*args, **kwargs)
        print("Have a great day!")
    return mfunc

# @greeting
def hello():
    print("Hello, World!")

@greeting
def name():
    print("My name is John Doe")


def add(a,b):
    print(f"The sum of {a} and {b} is {a+b}")

greeting(hello)()
greeting(add)(5,10)
greeting(name)()