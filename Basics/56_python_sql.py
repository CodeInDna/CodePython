# Python with sql

import sqlite3

# connect to database
# NOTE: if it couldn't find the specified file, it creates one when we execute this python file
conn = sqlite3.connect("my_friends.db")

# COMMANDS GOES HERE

# CREATE TABLE ******************
# create cursor object
c = conn.cursor()
# execute some sql

# create table
# c.execute("CREATE TABLE friends (fname TEXT, lname TEXT, closeness INTEGER)")

# insert query ******************************
# insert_query = "INSERT INTO friends (fname, lname, closeness) VALUES ('Ritu', 'Patel', 6)"
# c.execute(insert_query)

# BAD! DO NOT USE THIS!
# form_first = "Dinnie" 
# form_last = "Kairy" 
# form_closeness = 1 
# insert_query = f"INSERT INTO friends (fname, lname, closeness) VALUES('{form_first}','{form_last}','{form_closeness}')"
# c.execute(insert_query)

# BETTER WAY! Protects from SQL injection
# form_first = "John" 
# form_last = "Doe" 
# form_closeness = 4 
# insert_query = "INSERT INTO friends (fname, lname, closeness) VALUES (?, ?, ?)"
# c.execute(insert_query, (form_first, form_last, form_closeness))

# Bulk inserts in Python*********************
people = people = [
	("Roald","Amundsen", 5),
	("Rosa", "Parks", 8),
	("Henry", "Hudson", 7),
	("Neil","Armstrong", 7),
	("Daniel", "Boone", 3)]


# commit changes
conn.commit()

conn.close()