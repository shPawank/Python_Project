#Walrus Operator in python


# number=[1,2,3,4,5,6,7,8,9,10]

# while (n:=len(number))>0:
#     print(f"Length of the list is {n}")
#     number.pop()

# food=list()
# while True:
#     food_item=input("Enter a food item: ")
#     if food_item=='quit':
#         break
#     food.append(food_item)

#By walrus operator we can write the above code in a single line as follows:

food=list()
while (food_item:=input("Enter a food item: "))!='quit':
    food.append(food_item)
    