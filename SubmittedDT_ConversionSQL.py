import os
import time
import sys
import mysql.connector
from collections import deque



directory = 'C:\\Users\\cmc03\\OneDrive\\Desktop\\python'
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

        def insert_variables_into_table(SUBMITTED_DT,OLD_DOCUMENT):
            try:
                connection = mysql.connector.connect(host="localhost", user="root", passwd="root",database="advancedwalk", autocommit=True)
                cursor = connection.cursor()
                mySql_insert_query = """INSERT INTO prestage 
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
        