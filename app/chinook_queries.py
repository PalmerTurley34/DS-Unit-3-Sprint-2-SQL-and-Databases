import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT * FROM customers"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)