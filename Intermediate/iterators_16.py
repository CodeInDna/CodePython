#---------Iterators---------#
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)
# jay garrick
# barry allen
# wally west
# bart allen

# OR

# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))		# jay garrick
print(next(superhero))		# barry allen
print(next(superhero))		# wally west
print(next(superhero))		# bart allen

print('************************************')
# More Examples
# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))	# 0
print(next(small_value))	# 1
print(next(small_value))	# 2

#OR
# Loop over range(3) and print the values
for num in range(3):
    print(num)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))	# 0
print(next(googol))	# 1
print(next(googol)) # 2
print(next(googol)) # 3
print(next(googol)) # 4

print('************************************')

# There are also functions that take iterators and iterables as arguments. For example, the list() and sum() 
# functions return a list and the sum of elements, respectively.
# Create a range object: values
values = range(10, 21)

# Print the range object
print(values)		# range(10, 21)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)		# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)		# 165

print('************************************')
# enumerate*****************************************
# enumerate() returns an enumerate object that 
# produces a sequence of tuples, and each of the tuples is an index-value pair.
# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)	# [(0, 'charles xavier'), (1, 'bobby drake'), (2, 'kurt wagner'), (3, 'max eisenhardt'), (4, 'kitty pryde')]

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutant_list):
    print(index1, value1)
# 0 charles xavier
# 1 bobby drake
# 2 kurt wagner
# 3 max eisenhardt
# 4 kitty pryde

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)
# 1 charles xavier
# 2 bobby drake
# 3 kurt wagner
# 4 max eisenhardt
# 5 kitty pryde

print('************************************')

# zip*******************************************
# zip() takes any number of iterables and returns a 
# zip object that is an iterator of tuples. If you wanted to 
# print the values of a zip object, you can convert it into 
# a list and then print it. Printing just a zip object will not 
# return the values unless you unpack it first.
mutants = ['charles xavier',
 'bobby drake',
 'kurt wagner',
 'max eisenhardt',
 'kitty pryde']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy',
 'thermokinesis',
 'teleportation',
 'magnetokinesis',
 'intangibility']
# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)
# [('charles xavier', 'charles xavier', 'charles xavier'), ('bobby drake', 'bobby drake', 'bobby drake'), ('kurt wagner', 'kurt wagner', 'kurt wagner'), ('max eisenhardt', 'max eisenhardt', 'max eisenhardt'), ('kitty pryde', 'kitty pryde', 'kitty pryde')]

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)
# <zip object at 0x000002923CAC82C8>

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)
# charles xavier prof x telepathy
# bobby drake iceman thermokinesis
# kurt wagner nightcrawler teleportation
# max eisenhardt magneto magnetokinesis
# kitty pryde shadowcat intangibility


# There is no unzip function for doing the reverse of what zip() does. 
# We can, however, reverse what has been zipped together by using zip() 
# with a little help from *! * unpacks an iterable such as a list or a 
# tuple into positional arguments in a function call.
# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)
# ('charles xavier', 'telepathy') ('bobby drake', 'thermokinesis') ('kurt wagner', 'teleportation') ('max eisenhardt', 'magnetokinesis') ('kitty pryde', 'intangibility')

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)	# True
print(result2 == powers)	# True


# Processing large amounts of Twitter data
# Sometimes, the data we have to process reaches a size that is too 
# much for a computer's memory to handle. This is a common problem 
# faced by data scientists. A solution to this is to process an entire 
# data source chunk by chunk, instead of a single go all at once.
# Initialize an empty dictionary: counts_dict
import pandas as pd
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv("dataset/tweets.csv", chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)		# {'en': 97, 'et': 1, 'und': 2}


# Refactoring above example
# Define count_entries()
def count_entries2(csv_file,c_size,colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts2 = count_entries2("dataset/tweets.csv", 10, 'lang')

# Print result_counts
print(result_counts2)	# {'en': 97, 'et': 1, 'und': 2}