import os
#from itertools import groupby

#Assign folder to  variable 'directory'
#Open the variable 'directory' and display EACH .txt files as a list with no spaces
#This will ONLY be visible from the CMD line and will not affect the ACTUAL document.
#This is a good way to see where there are any notes and how they are being processed.
#Use this to see what files contain notes and seperate them to deal with later (If multiple lines exist or characters you do not want)
directory = 'C:\\path\\to\\folder'
for file in os.listdir(directory):
    if file.endswith(".txt"): #Skip non-TXT files
        with open(os.path.join(directory, file), "r") as f:
            nameList = [line.strip() for line in f]
            print(nameList)
            print('###################################################################')
