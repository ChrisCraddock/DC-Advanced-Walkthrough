import os
from collections import deque
from itertools import groupby


directory = 'C:\\Users\\cmc03\\OneDrive\\Desktop\\python'
for file in os.listdir(directory):
    if file.endswith(".txt"): #Skip non-TXT files
        with open(os.path.join(directory, file), "r") as f:
            nameList = [line.strip() for line in f]
            print(nameList)
            print('###################################################################')