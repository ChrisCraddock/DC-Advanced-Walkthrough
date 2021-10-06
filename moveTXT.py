import os
import shutil

#Source Folder
sourcepath='C:\\Users\\cmc03\\OneDrive\\Desktop\\python' 
sourcefiles = os.listdir(sourcepath)

#Destination Folder (must exist first)
destinationpath = 'C:\\Users\\cmc03\\OneDrive\\Desktop\\python\\newtext'
for file in sourcefiles:
    if file.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))

