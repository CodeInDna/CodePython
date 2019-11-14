#-----------File I/O-------------#

# Reading Files
# You can read a file with the open function
# open returns a file object to you
# You can read a file object with the read method

f = open("story.txt")
print(f)	#<_io.TextIOWrapper name='story.txt' mode='r' encoding='cp1252'>
# help(f)		# the details
print(f.read())

# In Terminal (PROBLEM!!!) : Why can't it read file "the second time"(giving an empty string)?
# >>> f = open("story.txt")
# >>> f.read()
# 'This short story is too short\n'
# >>> f.read()
# ''
# >>>
# Answer: Cursor Movement
# Python reads files by using a cursor
# This is like the cursor you see when you're typing
# After a file is read, the cursor is at the end
# To move the cursor, use the "seek" method
# >>> f.read()
# ''
# >>> f.seek(0)
# 0
# >>> f.read()
# "This short story is too short\nNow's it lil longer\nTHE END"
# >>> f.seek(1)
# 1
# >>> f.read()
# "his short story is too short\nNow's it lil longer\nTHE END"

# readline() is used to read line by line
# >>> f.read()
# ''
# >>> f.seek(0)
# 0
# >>> f.readline()
# 'This short story is too short\n'
# >>> f.readline()
# "Now's it lil longer\n"
# >>> f.readline()
# 'THE END'

# readlines() gives all the lines but in the form of list
# >>> f.seek(0)
# 0
# >>> f.readlines()
# ['This short story is too short\n', "Now's it lil longer\n", 'THE END']


# Closing a File
# You can close a file with the close method
# You can check if a file is closed with the close attribute
# Once closed, a file can't be read again
# >>> f.closed
# False
# >>> f.close()
# >>> f.closed
# True
# >>> f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.


# with Blocks
# using with statements, we don't have to manually close the file,
# it automatically does that for us
# >>> with open("story.txt") as file:
# ...     body = file.read()
# ...
# >>> file
# <_io.TextIOWrapper name='story.txt' mode='r' encoding='cp1252'>
# >>> file.closed
# True
# >>> body
# "This short story is too short\nNow's it lil longer\nTHE END"


# Writing to Text Files
# You can also use open to write to a file
# Need to specify the "w" flag as the second argument
# Original text overwritten with "w" flag
with open("story.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out\n")
# if the file is not present, it will create a new file and perform the 
# write operation

# File Modes
# r - Read a File(no writing) - this is the default
# w - writes and erases existing contents(if file is not present, it creates one)
# a - appends to end, preserving original contents(if file is not present, it creates one)
# r+ read and write to a file(writing based on cursor) (it gives an error if file is not present),it overwrites the text 

with open("story.txt", "a") as file:
	file.write("Hellooooooooo\n")
	
with open("story.txt", "r+") as file:
	file.write(":)")
	file.seek(10)
	file.write(":(")

# Exercise
# Copy the contents of story.txt to story_copy.txt
def copy(file_name, new_file_name):
	with open(file_name) as file:
		text = file.read()

	with open(new_file_name, "w") as new_file:
		new_file.write(text)

copy("story.txt", "story_copy.txt")

# Copy and reverse the contents of story.txt to story_copy_reverse.txt
def reverse(file_name, new_file_name):
	with open(file_name) as file:
		text = file.read()

	with open(new_file_name, "w") as new_file:
		new_file.write(text[::-1])

reverse("story.txt", "story_copy_reverse.txt")

# A fn which takes in a file name and returns a dict with number of lines,
# words, and characters in the file
def statistics(file_name):
	with open(file_name) as file:
		lines = file.readlines()
		words = sum(len(line.split(" ")) for line in lines)
		chars = sum(len(line) for line in lines)
	return {'lines':len(lines), 'words':words, 'characters':chars}
print(statistics('story.txt'))

# A fn which takes in a file name, old_word and a new-word
# Replaces all the instances of the word in the file with the replacement word
def find_replace(file_name, old_word, new_word):
	with open(file_name, "r+") as file:
		text = file.read()
		new_text = text.replace(old_word, new_word)
		file.seek(0)
		file.write(new_text)
		file.truncate()
print(find_replace('story.txt', "one", "1"))