#Merge the PDF
#Write a program to manipulate pdf files suing pyPDF. Your program should be able to merge multiple pdf files into a single pdf file.
#You are welcome to add more functionality.
#pypdf is free and open source library which is used to manipulate pdf files. You can install it using pip install pypdf.


#C:\Users\Asus\Desktop\Python_Project\my_Py_Code\ClutteredFolder\pawan_sbi_oayment.pdf

from PyPDF2 import PdfMerger
import os
merger = PdfMerger()
files = os.listdir("my_Py_Code/ClutteredFolder")
for file in files:
    if file.endswith(".pdf"):
        merger.append(f"my_Py_Code/ClutteredFolder/{file}")

merger.write("my_Py_Code/ClutteredFolder/merged.pdf")
merger.close()

