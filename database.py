

# import sqlite3
import sqlite3
# open a connection to the database
conn = sqlite3.connect('Northwind_small.sqlite')
# create a cursor to interact with the database. You can think of a cursor as a “handle” to the database that executes commands for you and returns information (if relevant-depends on the command).
cur = conn.cursor()
# use the cursor to execute commands
cur.execute('SELECT LastName, FirstName FROM Employee')
# access the results stored in the cursor
for row in cur:
  print(row[0],row[1])
# after we’re done, close the DB connection
conn.close()
