#Dictionary Methods in Python
#update()
info={
    "name":"Pawan",
    "age":20,
    "eligible": True
}

for item in info:
    print(item)

print(info)
info.update({"age":27})
print(info)
info.update({"DOB":"21Jan99"})
print(info)

ep1={
    123:55,
    453:54,
    126:69
}
ep2={
    456:45,
    654:44,
}
ep1.update(ep2)
print(ep1)

ep1.clear() #Empty the Dictionary
print(ep1)

ep2.pop(456)
print(ep2)

ep3={
    1:"pawan",
    2:"raman",
    3:"saman"
}
ep3.popitem()
print(ep3)

# del ep3
del ep3[1]
print(ep3)
