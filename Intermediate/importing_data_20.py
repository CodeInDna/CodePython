# Importing all text from the file***********

# Open a file: file
file = open("dataset/moby_dick.txt", mode='r')

# Print it
print(file.read())	# prints the content of file

# Check whether file is closed
print(file.closed)	# False

# Close file
file.close()

# Check whether file is closed
print(file.closed)	# True


# Importing text files line by line******************************
# For large files, we may not want to print all of their content to 
# the shell: we may wish to print only the first few lines. Enter 
# the readline() method, which allows us to do this. When a file called 
# file is open, you can print out the first line by executing 
# file.readline(). If you execute the same command again, the second 
# line will print, and so on.
# The concept of a context manager: you can bind a variable file by 
# using a context manager (with) construct, the variable file will be bound to that file.
# with helps us to close the file after the work is finished, we dont need to specify manually to close the file.
# Read & print the first 3 lines
with open('dataset/moby_dick.txt') as file:
    print(file.readline())	# prints line 1
    print(file.readline())	# prints line 2
    print(file.readline())	# prints line 3

# What are flat files?
# Flat file are the files which has attributes and records(rows)
# csv or txt files (tab seperated data) are flat files as they contain
# sueful data

# Importing flat files using Numpy
# Why Numpy?
# Numpy arrays: standard for storing numerical data
# Essential for other packages e.g.scikit-learn
# There are many functions which makes life easy
# loadtxt(), genfromtxt()

# Using loadtxt to import flat file data
# Import package
import numpy as np

# Assign filename to variable: file
file = 'dataset/mnist_kaggle_some_rows.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))	# <class 'numpy.ndarray'>
print(digits)

# Customizing your NumPy import
# What if there are rows, such as a header, that you don't want to 
# import? What if your file has a delimiter other than a comma? 
# What if you only wish to import particular columns?
# There are a number of arguments that np.loadtxt() takes that you'll 
# find useful:
# delimiter changes the delimiter that loadtxt() is expecting.
# You can use ',' for comma-delimited.
# You can use '\t' for tab-delimited.
# skiprows allows you to specify how many rows (not indices) you wish to skip
# usecols takes a list of the indices of the columns you wish to keep.
# Import numpy
# import numpy as np

# # Assign the filename: file
# file = 'digits_header.txt'	# Use any tab separated txt file	

# # Load the data: data
# data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# # Print data
# print(data)

# Importing different datatypes
# The file seaslug.txt
# has a text header, consisting of strings
# is tab-delimited.
# Due to the header, if you tried to import it as-is using np.loadtxt(),
# Python would throw you a ValueError and tell you that it could not 
# convert string to float. There are two ways to deal with this: 
# firstly, you can set the data type argument dtype equal to str 
# (for string).
# Assign filename: file
file = 'dataset/seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float)