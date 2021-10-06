import os
import shutil

#Source Folder
sourcepath='C:\\path\\to\\folder' 
sourcefiles = os.listdir(sourcepath)

#Destination Folder (must exist first)
destinationpath = 'C:\\path\\to\\new\\folder'
for file in sourcefiles:
    if file.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))

