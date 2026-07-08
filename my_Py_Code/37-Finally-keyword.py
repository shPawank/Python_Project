#37 Finally keyword in Python
from pprint import pprint
def func1():
    try:
        l=[1,2,3,4,5]
        i=int(input("Enter a number:"))
        print(l[i])
        return 1
    except:
        print("Invalid input")
        return 0

    finally:
        print("Finally...")
x=func1()
print(x)
