import PyPDF2
import os
import time

#Scan Directory
#Assign folder to  variable 'directory'
#Open the variable 'directory' and make a copy of all PDF files as a TXT file.
directory = 'C:\\path\\to\\folder'
for file in os.listdir(directory):
    if not file.endswith(".pdf"): #Skip non-PDF files
        continue
    with open(os.path.join(directory,file), 'rb') as pdfFileObj:  # Changes here
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        text=pageObj.extractText()
        print("Writing File "+ file +" to TXT.")
        file2=open(r"C:\path\to\folder\\"+file.replace('pdf','txt'),"a") #Write as TXT files.  Needs the double \\ at the end
        file2.writelines(text)
        print("Done saving.")
        file2.close()
        
