#35 For Loop with else in Python
for i in range(6):
    print(i)
    if i==5:
        break
else:
    print("empty")




for item in []:
    print(item)
else:
    print("Nothing to Print")


j=0
while j<5:
    print(j)
    j=j+1
    if j==2:
        break
else:
    print("empty")




for x in range(5):
    print("iteration  no {} in for loop".format(x+1))
else:
    print("empty")
print("Out of Loop")