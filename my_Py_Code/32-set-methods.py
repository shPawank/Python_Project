#Set Methods in Python
set1={2,5,9}
set2={3,4,7,8,9}
print("Update")
set1.update(set2)
print(set1)

print("Union")
set1=set1.union(set2)
print(set1)

print("Intersection ")
set1=set1.intersection(set2)
print(set1)

set3={"vns","sgo","ndls","gaya"}
set4={"sgo", "dli", "pryg","pat"}

set5=set3.symmetric_difference(set4)
print(set5)

#difference
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Delhi","Berlin","Madrid"}
cities3=cities.difference(cities2)
print(cities3)

print(cities.issubset(cities2))
print(cities.isdisjoint(cities2))


#add new element
cities.add("Pakistan")
print(cities)

cities.remove("Pakistan")
print(cities)

#Only clear the item not the set
# cities.clear()
# print(cities)

item=cities.pop()
print(cities)
print(item)

#del: is not a method, rather it is a keyboard which delete the set entirely
bucket={"Apple","Banana","Grapes","oranges"}
print(bucket)
del bucket
# print(bucket)
#nameerror

info={"Pawan",27,"Varanasi"}
if "Pawan" in info:
    print("pawan is in info")
else:
    print("pawan is not in info")

