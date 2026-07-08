#Static Methods in Python
#Static methods are methods that belong to a class rather than an instance of the class. 
#They can be called on the class itself, rather than on an instance of the class. 
#Static methods are defined using the @staticmethod decorator. 

class Math:
    def __init__(self, num):
        self.num = num

    def  addtonum(self, x):
        self.num =self.num + x



    @staticmethod
    def add(x, y):
        return x + y

# result = Math.add(5, 3)
# print(result)  # Output: 8  

a=Math(5)
print(a.num)  # Output: 5
a.addtonum(10)
print(a.num)  # Output: 15
print(a.add(9,10))
