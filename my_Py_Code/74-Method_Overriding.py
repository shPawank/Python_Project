#Method Overriding in Python
#Method overriding is a feature in object-oriented programming that allows a subclass to provide a specific implementation of 
#a method that is already defined in its superclass.
#When a method in a subclass has the same name, same parameters or signature, and same return type(or sub-type) as a method in 
#its superclass, then the method in the subclass is said to override the method in the superclass.

class Shape:
    def __init__(self, x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        super().__init__(radius,radius)  # Call the constructor of the superclass with dummy values

    def area(self):
        return 3.14 * super().area()  # Call the area method of the superclass and multiply by pi

rect=Shape(10,20)
print("Area of rectangle:",rect.area())

circle=Circle(5)
print("Area of circle:",circle.area())