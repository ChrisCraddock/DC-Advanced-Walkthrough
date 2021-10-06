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
            #print(nameList)

            
            
            queue = deque(nameList)
            NOTES = queue.pop()
            TITLE = str(file.strip('.txt'))

            # print(NOTES)
            # print(TITLE)

        def insert_variables_into_table(NOTE,OLD_DOCUMENT):
            try:
                connection = mysql.connector.connect(host="localhost", user="root", passwd="root",database="advancedwalk", autocommit=True)
                cursor = connection.cursor()
                mySql_insert_query = """INSERT INTO notes 
                    (NOTE,OLD_DOCUMENT)
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
        