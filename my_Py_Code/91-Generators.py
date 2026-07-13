#Generator in Python
def my_genrator():
    for i in range(500):
        yield i
gen=my_genrator()
for j in gen:
    print(j)