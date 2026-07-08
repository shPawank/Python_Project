#Getters and Setters

class myClass:
    def __init__(self, value):
        self.__value = value

    def show(self):
        print(f"Self value is {self.__value}")

    @property                               #getter
    def ten_value(self):
        return 10*self.__value

    @ten_value.setter                       #setter
    def ten_value(self, new_value):
        self.__value = new_value/10

obj1=myClass(10)
print(obj1.ten_value)
obj1.ten_value=20
obj1.show()
