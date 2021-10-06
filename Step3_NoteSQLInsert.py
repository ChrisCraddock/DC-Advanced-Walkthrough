import os
import time
import sys
import mysql.connector
from collections import deque

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
            #print(nameList)
            
            queue = deque(nameList)
            NOTES = queue.pop()
            TITLE = str(file.strip('.txt'))
            #Comment out everything below until you find what you need to include or exclude in the 'char_list' above
            # print(NOTES)
            # print(TITLE)
            
            #The passwd assumes you CHANGED the passwd to 'root'.  Leave change to blank or whatever the Database password is
            
            #Line 39: 'def insert_variables_into_table' are the COLUMN names in your database. They MUST match 'mySql_insert_query'
            #Line 46: 'record' are your VARIABLE names you created above. They need to be in the order of the COLUMNS they will go into.
            #Line 45: VALUES' %s is string formatting but just think of it as a vairable placeholder for 'record'.  It worked fine for 
            #both int and str in my database.  Only thing you need to make sure of is that the TYPE you are declaring above with the variable 
            #matches the TYPE in the database. Example int() = INT, str() = VARCHAR etc.
            #Line 61: 'insert_variables_into_table' at the bottom MUST match the variable names and order of 'record'
            #Explination: Essentially Line 61 'insert_variables_into_table()' is taking the variables assigned above and passing
            #them in Line 39 'def insert_variables_into_table()' as what the column names will be in your INSERT statement.
            #'record' takes Line 61 variables and uses what is inside them as the VALUES.  Sorry for any confussion in that explination.

        def insert_variables_into_table(NOTE,DOCUMENT_TITLE):
            try:
                connection = mysql.connector.connect(host="localhost", user="root", passwd="root",database="<database name>", autocommit=True)
                cursor = connection.cursor()
                mySql_insert_query = """INSERT INTO tableB 
                    (NOTE,DOCUMENT_TITLE)
                    VALUES (%s,%s)"""
                record = (NOTES,TITLE)
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

        insert_variables_into_table(NOTES,TITLE)

        time.sleep(2)
        
