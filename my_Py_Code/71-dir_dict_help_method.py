#dir, __dict__ and help method in Python
#dir() function returns a list of attributes and methods of any object (functions, modules, strings, lists, dictionaries etc.)
x=[1,2,3,4,5]
print(dir(x))
print(x.__add__)

#__dict__ attribute returns a dictionary of an object's attributes. It is useful tool for introspection and debugging. 
# It can be used to get the attributes of an object in a dictionary format.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
p=Person("Alice", 30)
print(p.__dict__)

#help() function is a built-in function in Python that provides information about a module, class, method, or function.
# It can be used to get information about the attributes and methods of an object, as well as the documentation for a module or function.
print(help(p))