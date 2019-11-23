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

# Importing flat files using Numpy**********************************
# Why Numpy?
# Numpy arrays: standard for storing numerical data
# Essential for other packages e.g.scikit-learn
# There are many functions which makes life easy
# loadtxt(), genfromtxt()

# Using loadtxt to import flat file data
# Import package
import numpy as np

# Assign filename to variable: file
file = 'dataset/digits.csv'

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


# Working with mixed datatypes (1)
# Much of the time you will need to import datasets which have 
# different datatypes in different columns; one column may contain 
# strings and another floats, for example. The function np.loadtxt() 
# will freak at this. There is another function, np.genfromtxt(), 
# which can handle such structures. If we pass dtype=None to it, it 
# will figure out what types each column should be.
# Here, the first argument is the filename, the second specifies the 
# delimiter , and the third argument names tells us there is a header. 
# Because the data are of different types, data is an object called a 
# structured array. Because numpy arrays have to contain elements that 
# are all the same type, the structured array solves this by being a 
# 1D array, where each element of the array is a row of the flat file 
# imported. You can test this by checking out the array's shape in the 
# shell by executing np.shape(data)
# Accessing rows and columns of structured arrays is super-intuitive: 
# to get the ith row, merely execute data[i] and to get the column with 
# name 'Fare', execute data['Fare'].
data = np.genfromtxt('dataset/titanic.csv', delimiter=',',names = True,dtype=None)
print(data["Survived"])


# Working with mixed datatypes (2)
# You have just used np.genfromtxt() to import data containing mixed datatypes. 
# There is also another function np.recfromcsv() that behaves similarly to np.genfromtxt(),
# except that its default dtype is None
# Import titanic.csv using the function np.recfromcsv() and assign it to the variable, d. You'll 
# only need to pass file to it because it has the defaults delimiter=',' and names=True in addition 
# to dtype=None!
# Assign the filename: file
file = 'dataset/titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])		# prints first three rows


# Importing flat files using Pandas**********************************
# Using pandas to import flat files as DataFrames (1)
# We are able to import flat files containing columns with different 
# datatypes as numpy arrays. However, the DataFrame object in pandas 
# is a more appropriate structure in which to store such data and, 
# thankfully, we can easily import files of mixed data types as 
# DataFrames using the pandas functions read_csv() and read_table().
# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'dataset/titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())	# prints first five observations


# Using pandas to import flat files as DataFrames (2)
# it is  straightforward to retrieve the corresponding numpy array 
# using the attribute values. 

# Assign the filename: file
file = 'dataset/digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file,nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)

# Print the datatype of data_array to the shell
print(type(data_array))
print(data_array[0])


# Customizing your pandas import
# The pandas package is also great at dealing with many of the issues 
# you will encounter when importing data as a data scientist, such as 
# comments occurring in flat files, empty lines and missing values. 
# Note that missing values are also commonly referred to as NA or NaN. 
# To wrap up this chapter, you're now going to import a slightly corrupted copy of the Titanic dataset titanic_corrupt.txt, which
# contains comments after the character '#'
# is tab-delimited.
# Assign filename: file
file = 'dataset/titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())
