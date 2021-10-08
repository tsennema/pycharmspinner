# This file is for manually inputting SQL queries to a database and printing the response
# Use Case: In terminal, python -i sqlquery.py
# Once in interactive terminal, query("example.db", "SELECT * FROM examples")

# SELECT queries will return the rows of results
# INSERT queries will return the new Primary key
# DELETE or UPDATE queries will return number of rows updated

import sqlite3
def query(db, query):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()
        print("Query successful")
        for row in result:
            print(row)
    except Exception as err:
        print(f"Error: '{err}'")