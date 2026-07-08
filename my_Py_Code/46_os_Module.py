#os Module in Python
#to open file for reading
import os
# if(not os.path.exists("myfolder")):
#     os.mkdir("myfolder")
#
# print("Welcome to my first lesson")
# for i in range(0,10):
#     os.rename(f"myfolder/Day{i+1}",f"myfolder/Tutor{i+1}")

folders=os.listdir("../../myfolder")
print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"myfolder/{folder}"))

print(os.getcwd())

for folder in folders:
    os.remove("myfolder/"+folder)

for folder in folders:
    os.rmdir(f"myfolder/{folder}")
