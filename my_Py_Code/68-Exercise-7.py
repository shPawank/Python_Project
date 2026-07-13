#Exercise 7 - Clear the Clutter
#WAP to clear the clutter inside a folder on your computer.
#You should use OS module to rename all png images from 1.png all the to the n.png where n is the number of images in the folder. 
#Do the same for all the other file types like .jpg, .jpeg, .txt, .pdf, .mp3, .mp4, .docx, etc.

import os

# os.rename("my_Py_Code/ClutteredFolder/1.txt", "my_Py_Code/ClutteredFolder/2.txt")

files = os.listdir("my_Py_Code/ClutteredFolder")
for file in files:
    if file.endswith(".png"):
        print(file)
    os.rename(f"my_Py_Code/ClutteredFolder/{file}", f"my_Py_Code/ClutteredFolder/{files.index(file)+1}.png")    
  