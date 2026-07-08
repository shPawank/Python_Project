#seek(), tell() and other functions

with open("../myfil2e.txt","r") as f:
    print(type(f))
    f.seek(20)
    data=f.read(2)
    print(data)
    f.close()


with open("../myfil2e.txt","r") as f:
    data=f.read(10)

    current_position=f.tell()
    f.seek(current_position)


#truncate fuction

with open("../myfil2e.txt","r") as f:
    f.write("Hello World")
    f.truncate(3)
    
with open("../myfil2e.txt","r") as f:
    print(f.read())
