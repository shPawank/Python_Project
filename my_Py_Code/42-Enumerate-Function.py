#Enumerate Function

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

marks=["14","56","1","98","87"]
# index=0
# for mark in marks:
#     print(mark)
#     if (index==3):
#         print("Awesome harry")
#     index=index+1
for index, mark in enumerate(marks):
    print(mark)
    if index==3:
        print("awesome")


subs=["Hindi","English","Math"]
for index, sub in enumerate(subs,start=1):
    print(index, sub)