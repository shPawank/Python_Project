#File IO in Python

#Reading to a File

f=open("../myfile.txt", "r")
print(f.read())
f.close()

# f=open("myfil2e.txt","w")

f=open("../myfile.txt", "w")
f.write("hello world")
# f.close()
f=open("../myfile.txt", "r")

#Writing to a File
f=open("../myfile.txt", "w")
f.write("hello world")
# f.close()
f=open("../myfile.txt", "r")

#Append to a File
f=open("../myfile.txt", "a")
f.write("hello world")


with open("../myfile.txt", "a"):
    f.write(": hello pawan")