## Data Center Advanced Walkthrough. Insert data from a PDF file into MySQL database

## This was used with XAMPP installed.

# Layout of database:

1. tableA: A1_A=smallint(6), A1_B=smallint(6), A1_C=smallint(6), SUBMITTED_DT=DateTime current_timestamp(), NOTE=tinytext null, DOCUMENT_TITLE=VARCHAR(30)
- This is to save space on tableA with long notes.
- NOTE will be given null by default in tableA, then compaire the DOCUMENT_TITLE in both and either given a 'Yes' or 'No'

2. tableB: NOTE=VARCHAR(150), DOCUMENT_TITLE=VARCHAR(30)
- tableC contains the DOCUMENT_TITLE and its DateTime conversion.
- It is then compaired with tableA's DOCUMENT_TITLE and UPDATE the SUBMITTED_DT column where both DOCUMENT_TITLE's exist

3. tableC: SUBMITTED_DT=DateTime, DOCUMENT_TITLE=VARCHAR(30)
- SUBMITTED_DT is not in Step4_Main_SQL_Insert_Statement.py. 
- This is created as a column in tableA and when a record is inserted, it automatically assigns the current_timestamp() of the SYSTEM it is on. 
- tableC replaces this if the TXT file is something like 'SITE_2001_01_01_2300' and the edits it to fit the format of DateTime as '2001-01-01 23:00:00'.

### NOTE is not in Step4_Main_SQL_Insert_Statement.py.
