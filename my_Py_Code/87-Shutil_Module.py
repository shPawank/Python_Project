#Shutil Module in python
#shutil module provides a number of high-level operations on files and collections of files. 
#In particular, functions are provided which support file copying and removal.

import shutil

# shutil.copy('my_Py_Code/85-command_line_utility.py','my_Py_Code/87-Shutil_Module.py')

shutil.copytree('my_Py_Code/lesson43.py','lesson43_copy.py') #copytree() method is used to copy an entire directory tree rooted at source (src) to the destination directory (dst).