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
# people = people = [
# 	("Roald","Amundsen", 5),
# 	("Rosa", "Parks", 8),
# 	("Henry", "Hudson", 7),
# 	("Neil","Armstrong", 7),
# 	("Daniel", "Boone", 3)]
# insert them altogether
# c.executemany("INSERT INTO friends VALUES(?, ?, ?)", people)

# insert by iterating
# average = 0
# for person in people:
# 	c.execute("INSERT INTO friends VALUES(?, ?, ?)", person)
# 	print("INSERTING DATA")
# 	average += person[2]
# print(average/len(people))

c.execute("SELECT * FROM friends")
# print(c)		# <sqlite3.Cursor object at 0x0000017B5A8C7960>
# for result in c:
# 	print(result)
# ('Ritu', 'Patel', 6)
# ...
# ('Daniel', 'Boone', 3)

# OR
res = c.fetchall()
print(res)	# It gives a list of tuples of data

# fetch one based on condition
c.execute("SELECT * FROM friends WHERE fname IS 'Ritu'")
res_one = c.fetchone()
print(res_one)	# ('Ritu', 'Patel', 6)

# select based on closeness and order it in ascending way
c.execute("SELECT * FROM friends WHERE closeness > 3 ORDER BY closeness")
print(c.fetchall())

# commit changes
conn.commit()

conn.close()