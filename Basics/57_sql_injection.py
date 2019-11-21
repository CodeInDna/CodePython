import sqlite3

# establish a connection to database
conn = sqlite3.connect("users.db")

# create a cursor object
c = conn.cursor()

# create a table
# query = "CREATE TABLE users (username, password)"
# c.execute(query)

# insert some data
# query = "INSERT INTO users (username, password) VALUES (?, ?)"
# c.execute(query, ('Lulu', 'Meow'))

# ask user for username and password
u = input("Enter your username please:.... ")
p = input("Enter your password please:.... ")

# BAD IDEA!
# query = f"SELECT * FROM users WHERE username = '{u}' AND password = '{p}'"	#  password: OR 1=1--(SQL INJECTION)

# GOOD ONE
query = "SELECT * FROM users WHERE username = ? AND password = ?"

c.execute(query, (u, p))

result = c.fetchone()
if result:
	print("WELCOME BACK!")
else:
	print("FAILED LOGIN!")


conn.commit()

# close the connection
conn.close()
