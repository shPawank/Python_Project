#Map, Filter and Reduce in Python

#MAP
def cube(x):
    return x*x*x
print(cube(5))

l=[1,2,3,4,5,6]
# new=[]
# for i in l:
#     new.append(cube(i))
# print(new)

# newl=list(map(cube,l))
# print(newl)

newl=map(lambda x:x*2,l)
print("Double", list(newl))


#FILTER
def filter_func(x):
    return x>2

# newnewl=list(filter(filter_func,l))
# print(newnewl)

newnewl=filter(lambda x:x>2,l)
print("Greater than 2", list(newnewl))

#REDUCE

from functools import reduce
number=[4,3,67,8,9]

def mysum(x,y):
    return x+y
# print(reduce(mysum,number))

total=reduce(mysum,number,0)
print(total)

