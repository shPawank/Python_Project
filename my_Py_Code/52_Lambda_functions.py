#Lambda functions in Python

# def double(x):
#     return x*2

double=lambda x: x*2

cube=lambda x: x**3

avg=lambda x,y:(x+y)/2


def run(fx,value):
    return 10+fx(value)


print(double(4))
print(cube(4))
print(avg(4,8))

print(run(cube, 10))
