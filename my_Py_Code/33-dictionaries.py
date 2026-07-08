#Dictionaries in Python
#Dictionary are ordered collection of data items.
#That store multiple items in single variable.
# #Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets.

info={
    'name':'Pawan',
    'age':27,
    'eligible':True
}
print(info['name'])         #Pawan
print(info.get('name'))     #Pawan
print(info)                 #{'name': 'Pawan', 'age': 27, 'eligible': True}

print(info.keys())
print(info.values())


print(info.items())

for key,value in info.items():
    print(key,value)

print("--using loop--")
for key in info:
    print(key)

for key in info.keys():
    print(f" the value corresponding the {key} is {info[key]}" )


for items in info.values():
    print(items)