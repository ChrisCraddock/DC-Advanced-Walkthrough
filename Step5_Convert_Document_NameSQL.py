import os
import time
import sys
import mysql.connector
from collections import deque


#Assign the path to a variable.  For-loop all the .txt files
directory = 'C:\\path\\to\\folder'
for file in os.listdir(directory):
    if file.endswith(".txt"): #Skip non-TXT files
        with open(os.path.join(directory, file), "r") as f:
            nameList = [line.strip() for line in f]
           #Create TITLE from the document title
            TITLE = str(file.strip('.txt'))
            #Put the title into a List
            title_date=list(TITLE)

            #Use deque and assign it as Queue
            queue = deque(title_date)
            skipC = str(queue.popleft())
            skipL = str(queue.popleft())
            skipT = str(queue.popleft())
            skipSite = str(queue.popleft())
            skip_ = str(queue.popleft())
            year1 = str(queue.popleft())
            year2 = str(queue.popleft())
            year3 = str(queue.popleft())
            year4 = str(queue.popleft())
            skip_ = str(queue.popleft())
            month1 = str(queue.popleft())
            month2 = str(queue.popleft())
            skip_ = str(queue.popleft())
            day1 = str(queue.popleft())
            day2 = str(queue.popleft())
            skip_ = str(queue.popleft())
            hour1 = str(queue.popleft())
            hour2 = str(queue.popleft())
            minute1 = str(queue.popleft())
            minute2 = str(queue.popleft())
            
            New_DateTime = year1+year2+year3+year4+'-'+month1+month2+'-'+day1+day2+' '+hour1+hour2+':'+minute1+minute2+':00'

            #The passwd assumes you CHANGED the passwd to 'root'.  Leave change to blank or whatever the Database password is
            
            #Line 56: 'def insert_variables_into_table' are the COLUMN names in your database. They MUST match 'mySql_insert_query'
            #Line 63: 'record' are your VARIABLE names you created above. They need to be in the order of the COLUMNS they will go into.
            #Line 62: VALUES' %s is string formatting but just think of it as a vairable placeholder for 'record'.  It worked fine for 
            #both int and str in my database.  Only thing you need to make sure of is that the TYPE you are declaring above with the variable 
            #matches the TYPE in the database. Example int() = INT, str() = VARCHAR etc.
            #Line 78: 'insert_variables_into_table' at the bottom MUST match the variable names and order of 'record'
            #Explination: Essentially Line 78 'insert_variables_into_table()' is taking the variables assigned above and passing
            #them in Line 56 'def insert_variables_into_table()' as what the column names will be in your INSERT statement.
            #'record' takes Line 78 variables and uses what is inside them as the VALUES.  Sorry for any confussion in that explination.
            
        def insert_variables_into_table(SUBMITTED_DT,OLD_DOCUMENT):
            try:
                connection = mysql.connector.connect(host="localhost", user="root", passwd="root",database="<database name>", autocommit=True)
                cursor = connection.cursor()
                mySql_insert_query = """INSERT INTO tableC 
                    (SUBMITTED_DT,OLD_DOCUMENT)
                    VALUES (%s,%s)"""
                record = (New_DateTime,TITLE)
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

        insert_variables_into_table(New_DateTime,TITLE)

        #time.sleep(2)
        
