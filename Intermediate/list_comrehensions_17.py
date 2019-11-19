# List Comrehensions
# Collapse for loops for building lists into a single line
# Components
	# Iterable
	# Iterator variable(represent member of iterable)
	# Output Expression
# Create list comprehension: squares
squares = [i ** 2 for i in range(0,10)]
print(squares)	# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print('************************************')

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[row for row in range(0,5)] for col in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]

print('************************************')

# Advanced Comrehensions
# Using conditionals in comprehensions
# Syntax : [ output expression for iterator variable in iterable if predicate expression ]
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# with if and else both
new_fellowship_else = [member if len(member)>=7 else ""  for member in fellowship]

# Print the new list
print(new_fellowship)	# ['samwise', 'aragorn', 'legolas', 'boromir']
print(new_fellowship_else)	# ['', 'samwise', '', 'aragorn', 'legolas', 'boromir', '']

print('************************************')

# Dict Comprehension
# The main difference between a list comprehension and a dict 
# comprehension is the use of curly braces {} instead of []. 
# Additionally, members of the dictionary are created using a colon :, 
# as in <key> : <value>.
# Create dict comprehension: new_fellowship
new_fellowship_dict = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship_dict)	# {'frodo': 5, 'samwise': 7, 'merry': 5, 'aragorn': 7, 'legolas': 7, 'boromir': 7, 'gimli': 5}

print('************************************')



