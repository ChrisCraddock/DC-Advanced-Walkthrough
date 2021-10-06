import os
import time
import sys
import mysql.connector
from collections import deque
from itertools import groupby


directory = 'C:\\Users\\cmc03\\OneDrive\\Desktop\\python'
for file in os.listdir(directory):
    if file.endswith(".txt"): #Skip non-TXT files
        with open(os.path.join(directory, file), "r") as f:
            nameList = [line.strip() for line in f]
            transferlist = nameList
            char_list=['UPS A','PDU A1','PDU B1','CRAC 03','PDU A2','CRAC 05','UPS B',
            'PDU B2','CRAC 06','ATS 1','ATS 2','CRAC 02','CRAC 04','CRAC 01','a','b','c','d','e',
            'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
            'w','x','y','z','/',':']
            transferlist2=[ele for ele in transferlist if all(ch not in ele for ch in char_list)]

            print(nameList)
            print(transferlist2)
            
            
            queue = deque(nameList)
            popList = queue.popleft()
            popList = queue.popleft()
            popList = queue.popleft()
            popList = queue.popleft()
            SubmittiontName = queue.popleft()
            popList = queue.popleft()
            skipDateTime = queue.popleft()
            USER = SubmittiontName
            DATE = skipDateTime
            queue = deque(transferlist2)
            UPS_A_KW = int(queue.popleft())
            A1_A = int(queue.popleft())
            A1_B = int(queue.popleft())
            A1_C = int(queue.popleft())
            A1_kVA = int(queue.popleft())
            B1_A = int(queue.popleft())
            B1_B = int(queue.popleft())
            B1_C = int(queue.popleft())
            B1_kVA = int(queue.popleft())
            CRAC03TEMP = int(queue.popleft())
            CRAC03HUM = int(queue.popleft())
            A2_A = int(queue.popleft())
            A2_B = int(queue.popleft())
            A2_C = int(queue.popleft())
            A2_kVA = int(queue.popleft())
            CRAC05TEMP = int(queue.popleft())
            CRAC05HUM = int(queue.popleft())
            UPS_B_KW = int(queue.popleft())
            B2_A = int(queue.popleft())
            B2_B = int(queue.popleft())
            B2_C = int(queue.popleft())
            B2_kVA = int(queue.popleft())
            CRAC06TEMP = int(queue.popleft())
            CRAC06HUM = int(queue.popleft())
            popList = int(queue.popleft())
            popList = int(queue.popleft())
            popList = int(queue.popleft())
            popList = int(queue.popleft())
            CRAC02TEMP = int(queue.popleft())
            CRAC02HUM = int(queue.popleft())
            CRAC04TEMP = int(queue.popleft())
            CRAC04HUM =int(queue.popleft())
            CRAC01TEMP = int(queue.popleft())
            CRAC01HUM = int(queue.popleft())
            #NOTES = str(file.strip('.txt'))
            TITLE = str(file.strip('.txt'))

        def insert_variables_into_table(UPS_A_KW,A1_A,A1_B,A1_C,A1_kVA,B1_A,B1_B,B1_C,B1_kVA,CRAC03TEMP,
                    CRAC03HUM,A2_A,A2_B,A2_C,A2_kVA,CRAC05TEMP,CRAC05HUM,UPS_B_KW,B2_A,
                    B2_B,B2_C,B2_kVA,CRAC06TEMP,CRAC06HUM,CRAC02TEMP,CRAC02HUM,CRAC04TEMP,
                    CRAC04HUM,CRAC01TEMP,CRAC01HUM,SUBMITTED_BY,OLD_DOCUMENT):
            try:
                connection = mysql.connector.connect(host="localhost", user="root", passwd="root",database="advancedwalk", autocommit=True)
                cursor = connection.cursor()
                mySql_insert_query = """INSERT INTO clt1 
                    (UPS_A_KW,A1_A,A1_B,A1_C,A1_kVA,B1_A,B1_B,B1_C,B1_kVA,CRAC03TEMP,
                    CRAC03HUM,A2_A,A2_B,A2_C,A2_kVA,CRAC05TEMP,CRAC05HUM,UPS_B_KW,B2_A,
                    B2_B,B2_C,B2_kVA,CRAC06TEMP,CRAC06HUM,CRAC02TEMP,CRAC02HUM,CRAC04TEMP,
                    CRAC04HUM,CRAC01TEMP,CRAC01HUM,SUBMITTED_BY,OLD_DOCUMENT)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                record = (UPS_A_KW,A1_A,A1_B,A1_C,A1_kVA,B1_A,B1_B,B1_C,B1_kVA,CRAC03TEMP,
                    CRAC03HUM,A2_A,A2_B,A2_C,A2_kVA,CRAC05TEMP,CRAC05HUM,UPS_B_KW,B2_A,
                    B2_B,B2_C,B2_kVA,CRAC06TEMP,CRAC06HUM,CRAC02TEMP,CRAC02HUM,CRAC04TEMP,
                    CRAC04HUM,CRAC01TEMP,CRAC01HUM,USER,TITLE)
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

        insert_variables_into_table(UPS_A_KW,A1_A,A1_B,A1_C,A1_kVA,B1_A,B1_B,B1_C,B1_kVA,CRAC03TEMP,
                    CRAC03HUM,A2_A,A2_B,A2_C,A2_kVA,CRAC05TEMP,CRAC05HUM,UPS_B_KW,B2_A,
                    B2_B,B2_C,B2_kVA,CRAC06TEMP,CRAC06HUM,CRAC02TEMP,CRAC02HUM,CRAC04TEMP,
                    CRAC04HUM,CRAC01TEMP,CRAC01HUM,USER,TITLE)

        time.sleep(2)
        