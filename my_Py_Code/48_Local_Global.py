#Local vs Global Variables in Python

r=45
print(r)
def hello():
    r=5
    print(f"local r is {r}")
    print("Hello Pawan")

print(f"the global is {r}")
hello()
print(f"the global is {r}")



































# x=20
# def my_func():
#     y=56
#     print(x)
#     print(y)
# my_func()
# print(x)
# # print(y)        #NameError: name 'y' is not defined
#
# #The global Keyword
# count=0
# def increment(x):
#     global count        #Declare intent to modify global
#     count+=1
# increment(x)
# increment(x)
# print("count", count)
#
# # The nonlocal Keyword
# # Used in nested functions to modify a variable from the enclosing (but non-global) scope:
# def outer_func():
#     x=34
#     def inner_func():
#         nonlocal x
#         x+=5
#     inner_func()
#     print(x)
# outer_func()