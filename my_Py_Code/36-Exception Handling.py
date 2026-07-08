#Exception Handling in Python
a= input("Enter a number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={int(a)*i}")
except Exception as e:
    print(e)
print("Hey There")



try:
    num = int(input("Enter a number: "))
    a=[3,5]
    print(a[num])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Index out of bound")
