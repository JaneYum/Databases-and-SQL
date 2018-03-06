

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


#Print all of the company names that are located in Western Europe.
cur1 = conn.cursor()
cur1.execute('SELECT CompanyName FROM Supplier WHERE Region="Western Europe"')
for row in cur1:
  print(row[0])
#Print all of the names of products that are discontinued.
cur2 = conn.cursor()
cur2.execute('SELECT ProductName FROM Product WHERE discontinued=1')
for row in cur2:
  print(row[0])
#Print all of the employees that report to Andrew Fuller.
cur3 = conn.cursor()
cur3.execute('SELECT Id FROM Employee WHERE ReportsTo=2')
for row in cur3:
  print(row[0])
#Print the order date and shipped date for all orders that were/are destined for the USA.
cur4 = conn.cursor()
cur4.execute('SELECT OrderDate,ShippedDate FROM [Order] WHERE ShipCountry="USA"')
for row in cur4:
  print(row[0])

# after we’re done, close the DB connection
conn.close()
