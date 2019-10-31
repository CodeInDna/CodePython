#---------------List--------------#

#---------Creating List-----------#
my_stuff = ["socks", 100, "crop top", "50"]

nums = list(range(1, 100))


#-------Accessing List Data-------#
people = ['Hanna', 'Louise', 'Claudia', 'Angela', 'Geoffrey', 'aparna']
#change list data
people[0] = 'Hannah'
people[4] = 'Jeffrey'
people[-1] = 'Aparna' # Or people[5] = 'Aparna'
print(people)


#------Iteration Over List-------#
people = ['Hanna', 'Louise', 'Claudia', 'Angela', 'Geoffrey', 'aparna']
# for loop
for friends in people:
	print(friends)

numbers = [1, 2, 3, 4, 5, 6]
# for loop
for number in numbers:
	print(number ** 2)

sounds = ["super","cali", "fragile", "istic", "expi", "ali", "docious"]
large_string = ""
for sound in sounds:
	large_string += sound.upper()
print(f"{large_string}") 

# while loop
i = 0
while i < len(numbers):
	print(numbers[i])
	i += 1 

# list methods
# 1. append (if u want to add 1 item to the end of the list)
instructors = ["John", "Mahi", "Virat", "Ranveer"]
instructors.append('Micheal')

# 2. extend (if u want to add multiple item to the end of the list)
instructors.extend(['Jacob', 'Virat', 'Deepika'])

# 3. insert (insert an item at a given position)
instructors.insert(2, 'Anushka')

print(f"{instructors}")


# 4. clear	(clear everything from the list)
names = ['julie', 'peter', 'maria']
names.clear()
print(f"{names}")

# 5. pop    (remove the last item when index not given otherwise removes the item at the given index and return the item)
instructors.pop()
print(f"{instructors}")

# 6. remove	(remove the first matching item from the list)
instructors.remove('Virat')
print(f"{instructors}")

# 7. index	(returns the index of the specified item in the list)
print(instructors.index('Virat'))

# 8. count	(returns the number of times x appears in the list)
names = ['julie', 'peter', 'maria', 'julie', 'colt', 'julie']
print(names.count('julie'))

# 9. reverse(reverse the elements in the original list )
names.reverse()
print(names)

# 10. sort  (sort the items of the list in asc order (in place))
names.sort()
print(names)

# 11. join(string method)  (convert list into string)
friends = ', '.join(names)
print(friends)

# slicing (access the part of the old list and make a new list) list_name[start:end:step]
#start parameter (start counting from 0)
colors = ["red", "orange", "green", "blue", "teal", "turquoise", "white", "black"]
new_palette1 = colors[2:]	# ["green", "blue", "teal", "turquoise", "white", "black"]
new_palette2 = colors[-2:]	# ["white", "black"]
print(new_palette1)
print(new_palette2)

#end parameter (does not consider the last index just like range)
first_list = [1,2,3,4]
print(first_list[:2])	# [1,2]
print(first_list[:4])	# [1,2,3,4]
print(first_list[1:3])	# [2,3]
print(first_list[:-1])	# [1,2,3] (items exclude from the end)
print(first_list[1:-1])	# [2,3] (items exclude from the end)

#step (the number to count at a time just like in range)
second_list = [1,2,3,4,5,6,7]
print(second_list[1::2]) # [2,4,6]
print(second_list[::2]) # [1,3,5,7]
print(second_list[1::-1]) # [2,1]
print(second_list[:1:-1]) # [7,6,5,4,3,2]
print(second_list[2::-1]) # [3,2,1]

# we can reverse a list or string
print(second_list[::-1])

# we can modify a list or string
second_list[1:4] = ['a','b','c']
print(second_list)

#swapping values
names = ["James", "Micheal"]
names[0], names[1] = names[1], names[0]
print(names)