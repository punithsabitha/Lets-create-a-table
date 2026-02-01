# connect with sql database
# Import necessary libraraies
import sqlite3
import pandas as pd

conn = sqlite3.connect('database.sqlite')
print("Opened data sucessfully")
conn.execute("DROP TABLE IF EXISTS CLASS_10")
# Create a new table in given database with mentioned constraints
conn.execute('''CREATE TABLE CLASS_10(
SNO INT PRIMARY KEY NOT NULL,
Roll_No INT NOT NULL,
Name TEXT NOT NULL,
AGE INT DEFAULT (15),
GENDER TEXT NOT NULL,
Email_ID TEXT NOT NULL,
Contact_No REAL NOT NULL);''')

print("Table created successfully")

# Enter data for 3 different entries
conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) VALUES (1, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8080900);")

conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) VALUES (2, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900 );")

conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) VALUES (3, 3, 'Rajo', 15, 'Male', 'allen@gmail.com', 9900900 );")

# Step 4: Save the changes
conn.commit()
print("Records created sucessfully")

# Step 5: Display all tables in the database
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("\nTables in database:")
print(tables)

# Step 6: Read data from CLASS_10 table
class_10d = pd.read_sql("SELECT * FROM CLASS_10;", conn)
print("\nCLASS_10 table data:")
print(class_10d)

# Step 7: Close the connection
conn.close()
print("\nConnection closed.")
