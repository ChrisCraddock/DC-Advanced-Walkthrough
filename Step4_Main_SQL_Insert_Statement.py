import os
import time
import sys #May not need this since os is imported but it won't hurt anything if left in.
import mysql.connector
from collections import deque
from itertools import groupby

#Assign the path to a variable.  For-loop all the .txt files
directory = 'C:\\path\\to\\folder'
for file in os.listdir(directory):
    if file.endswith(".txt"): #Skip non-TXT files
        with open(os.path.join(directory, file), "r") as f:
            nameList = [line.strip() for line in f]
            transferlist = nameList
            char_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
            'w','x','y','z','/',':',<any words you would like to exclude that may have not been picked up>]
            
            #Create a new variable and list from all the excluded items
            transferlist2=[ele for ele in transferlist if all(ch not in ele for ch in char_list)]
            
            #Print the TXT file as one large list. Comment out when satistfied
            print(nameList)
            
            #Print a NEW list with the 'char_list' words excluded. Comment out when satistfied
            print(transferlist2)
            
            #Comment out everything below until you find what you need to include or exclude in the 'char_list' above
            
            #Repeat popList until you get to what you need from the 'nameList' (unedited list 1st).
            #Assighn variables to everything else, if any, you need.  Exmples: Names, Dates etc..
            queue = deque(nameList)
            popList = queue.popleft()
            
            #Create variables for items in 'transferlist2'.  Starting examples below
            queue = deque(transferlist2)
            A1_A = int(queue.popleft())
            A1_B = int(queue.popleft())
            A1_C = int(queue.popleft())
            #....
            #Skip adding notes here if you do not need them or if you want to add them to 
            #a seperate Table later (see NoteCheck.py and/or NoteSQLInsert.py)
            #NOTES = str(file.strip('.txt'))
            
            #Last variable inserts the name of the .txt file minus the extension
            TITLE = str(file.strip('.txt'))

            #The passwd assumes you CHANGED the passwd to 'root'.  Leave change to blank or whatever the Database password is
            
            #Line 59: 'def insert_variables_into_table' are the COLUMN names in your database. They MUST match 'mySql_insert_query'
            #Line 66: 'record' are your VARIABLE names you created above. They need to be in the order of the COLUMNS they will go into.
            #Line 65: VALUES' %s is string formatting but just think of it as a vairable placeholder for 'record'.  It worked fine for 
            #both int and str in my database.  Only thing you need to make sure of is that the TYPE you are declaring above with the variable 
            #matches the TYPE in the database. Example int() = INT, str() = VARCHAR etc.
            #Line 81: 'insert_variables_into_table' at the bottom MUST match the variable names and order of 'record'
            #Explination: Essentially Line 81 'insert_variables_into_table()' is taking the variables assigned above and passing
            #them in Line 59 'def insert_variables_into_table()' as what the column names will be in your INSERT statement.
            #'record' takes Line 81 variables and uses what is inside them as the VALUES.  Sorry for any confussion in that explination.
            
        def insert_variables_into_table(A1_A,A1_B,A1_C,DOCUMENT_TITLE):
            try:
                connection = mysql.connector.connect(host="localhost", user="root", passwd="root",database="<database name>", autocommit=True)
                cursor = connection.cursor()
                mySql_insert_query = """INSERT INTO <TABLE NAME> 
                    (A1_A,A1_B,A1_C,DOCUMENT_TITLE)
                    VALUES (%s,%s,%s,%s)"""
                record = (A1_A,A1_B,A1_C,TITLE)
                cursor.execute(mySql_insert_query,record)
                connection.commit()
                print("Connection Open")
                print("Record Inserted Successfully")
            
            except mysql.connector.Error as error:
                print("Failed to insert {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("Connection Closed")

        insert_variables_into_table(A1_A,A1_B,A1_C,TITLE)

        time.sleep(2) #This can be commented out if you are not worried about resources
        
