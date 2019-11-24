# Relational Database
# Based on relational model of data
# First described by Edgar "Ted" Codd

# Relational Database Management Systems
# SQLite
# Mysql
# Postgres

# Creating a database engine in Python
# SQLite database: Fast and simple
# SQLAlchemy: Works with many Relational Databse Management Systems
# We'll create an engine to connect to the SQLite database 
# 'Chinook.sqlite'.Here, 'sqlite:///Chinook.sqlite' is called the 
# connection string to the SQLite database Chinook.sqlite.the Chinook 
# database contains information about a semi-fictional digital media 
# store in which media data is real and customer, employee and sales data has been manually created.
from sqlalchemy import create_engine

# create engine
engine = create_engine('sqlite:///dataset/Chinook.sqlite')
# the Chinook database contains information about a semi-fictional digital media store in which media 
# data is real and customer, employee and sales data has been manually created.

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)	# ['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']


# Queying Relational Databases in Python
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///dataset/Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Album")

# Save results of the query to DataFrame: df
df2 = pd.DataFrame(rs.fetchall())

# print(df)
# Close connection
con.close()

# Customizing SQL Queries
# Perform query and save results to DataFrame: df
with engine.connect() as conn:
	rs = conn.execute("SELECT LastName,Title from Employee")
	df = pd.DataFrame(rs.fetchmany(3))
	df.columns = rs.keys()
# Print the length of the DataFrame df
# print(len(df))	# 3
# Print the head of the DataFrame df
# print(df.head())	
#   LastName                Title
# 0    Adams      General Manager
# 1  Edwards        Sales Manager
# 2  Peacock  Sales Support Agent


# Filtering your database records using SQL's WHERE
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee WHERE EmployeeId >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
# print(df.head())

# Ordering your SQL records with ORDER BY
# Open engine in context manager
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee ORDER BY BirthDate ASC")
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
# print(df.head())


# Querying relational databases directly with pandas
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///dataset/Chinook.sqlite')

df1 = pd.read_sql_query("SELECT * FROM Album", engine)

# print(df1.head())
#    AlbumId                                  Title  ArtistId
# 0        1  For Those About To Rock We Salute You         1
# 1        2                      Balls to the Wall         2
# 2        3                      Restless and Wild         2
# 3        4                      Let There Be Rock         1
# 4        5                               Big Ones         3
# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df2 = pd.DataFrame(rs.fetchall())
    df2.columns = rs.keys()
# print(df2.equals(df1))	# True

# Advanced Querying: Exploiting table relationships
# Joining Tables
# Inner Join
query = '''SELECT Title, Name FROM Album INNER JOIN Artist ON 
		Album.ArtistID=Artist.ArtistID'''
df = pd.read_sql_query(query, engine)
print(df.head())
#                                    Title       Name
# 0  For Those About To Rock We Salute You      AC/DC
# 1                      Balls to the Wall     Accept
# 2                      Restless and Wild     Accept
# 3                      Let There Be Rock      AC/DC
# 4                               Big Ones  Aerosmith