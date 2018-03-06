# Databases-and-SQL


- What is a database?
  - Simply: a computer file that stores data
    - A spreadsheet, csv, json file, or even plain text file can be considered a “database” if it’s purpose is to store data
  - What we think of as a “database” has particular features
    - Structure to make it easy to access data in different ways (using different fields)
    - Allowing updates from multiple sources simultaneously
    - Enforcing data integrity (e.g., always using the same data type, format, etc.)
    
# database structure 
  a Row describes a particular Entity
  a Table will contain data for a particular type of Entity
  Columns have particular data types. Examples include:
    - TEXT
    - NUMERIC
    - INTEGER
    - REAL
    - BLOB
  the database we’ll be using, sqlite, only supports these 5. 
  Other DBs support other data types as well, such as DATETIME or BOOLEAN. 
  
 
# sqlite
There are many different types of database software out there. Some of the most popular that you will run into include:

- MySQL (free)
- PostgresSQL (free)
- MSFT SQL Server (not free)
- Oracle (not free)
see the structure of the data
ID define the relationship between the data

# SQL“Sequel”
- It’s not quite a programming language. It’s “declarative” but not “procedural.”
  - You can’t write a full program with SQL
  - You have to use it with something else (e.g., DB Browser, python)
- SQL lets you
  - Create databases and database structures (e.g., Tables)
  - Put stuff into databases
  - Update stuff that’s already in databases
  - Query stuff that’s in databases
  # SQL - Queries
  1. SELECT * FROM Employee
- SELECT: introduces a clause that tells SQL that we are querying (or “selecting”) a subset of data from the DB
- FROM: tells SQL the location of the data from which we are selecting (e.g., the Table)
- *: a wildcard that means “select all”--in this case it means “select all columns” *
  2. SELECT LastName, FirstName FROM Employee 
  - Instead of ‘*’ we specified ‘LastName, FirstName.’
  3. SELECT LastName, FirstName FROM Employee WHERE Title='Sales Representative'
  WHERE: introduces selection criteria. The stuff after WHERE will resolve to True or False for each row in the DB that is examined. 


  
  # SQL - Case-sensitivity
  SQL commands are not case sensitive.
  Table names and Column names are sometimes case sensitive. This actually depends on the database.

# Searching DBs in Python
  the python file should be in the same directory with the database file
  tip:
  Creating strings on multiple lines. 
    statement = 'SELECT LastName, FirstName '
    statement += 'FROM Employee '
    statement += 'WHERE Title="Sales Representative"'
    cur.execute(statement)
  Nesting strings within strings.
  # cursor
  You’ll note that after we executed the SQL command, we just iterated through the cursor as if it were a list.   This is a nice little feature that the cursor object gives us—you can treat it as an iterator which is    
  pythonic for “something that can act like a list.” It’s not actually a list, though. For example, you can’t     call len(cur).
      cur.fetchone() # gets the "next" row in the cursor, or None if there are none left
      cur.fetchall() # gets all of the "remaining" rows in the cursor as a list
      cur.fetchmany(size=N) # gets N rows as a list
  
  
  
  

  
  
