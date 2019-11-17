# ------------------Pandas(A Package)-------------------
# Pandas is an open source library, providing high-performance, 
# easy-to-use data structures and data analysis tools for Python. 

# The DataFrame is one of Pandas' most important data structures. 
# It's basically a way to store tabular data where you can label 
# the rows and the columns. One way to build a DataFrame is from a 
# dictionary.

# Difference between pandas and Numpy
# Numpy : One Data Type
# Pandas : * Accept multiple data Type
# 		 * High level data manipulation tool
# 		 * We McKinney
# 		 * Built on Numpy

# Two ways to create DataFrame using pandas


# 1st - DataFrame from Dictionary(Manually)
# In the exercises that follow we will be working with vehicle data from 
# different countries. Each observation corresponds to a country and the 
# columns give information about the number of vehicles per capita, 
# whether people drive left or right, and so on.

# Three lists are defined in the script:
# * names, containing the country names for which data is available.
# * dr, a list with booleans that tells whether people drive left or right in the corresponding country.
# * cpc, the number of motor vehicles per 1000 people in the corresponding country.
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)
#    cars_per_cap        country  drives_right
# 0           809  United States          True
# 1           731      Australia         False
# 2           588          Japan         False
# 3            18          India         False
# 4           200         Russia          True
# 5            70        Morocco          True
# 6            45          Egypt          True


# Notice: The row labels (i.e. the labels for the different observations) 
# were automatically set to integers from 0 up to 6?

# We can specify row labels of the cars DataFrame. We do this by setting 
# the index attribute of cars, that can access as cars.index.
# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
#      cars_per_cap        country  drives_right
# US            809  United States          True
# AUS           731      Australia         False
# JPN           588          Japan         False
# IN             18          India         False
# RU            200         Russia          True
# MOR            70        Morocco          True
# EG             45          Egypt          True


# 2nd - DataFrame from csv file(Direct)
# Putting data in a dictionary and then building a DataFrame works,
# but it's not very efficient. What if you're dealing with millions 
# of observations? In those cases, the data is typically available 
# as files with a regular structure. One of those file types is the 
# CSV file, which is short for "comma-separated values".

cars = pd.read_csv('dataset/cars.csv')
print(cars)
#   Unnamed: 0  cars_per_cap        country  drives_right
# 0         US           809  United States          True
# 1        AUS           731      Australia         False
# 2        JAP           588          Japan         False
# 3         IN            18          India         False
# 4         RU           200         Russia          True
# 5        MOR            70        Morocco          True
# 6         EG            45          Egypt          True

# the output is not entirely what we wanted. The row labels were 
# imported as another column without a name.

# Remember index_col, an argument of read_csv(), that you can use to 
# specify which column in the CSV file should be used as a row label?

# Fix import by including index_col
cars = pd.read_csv('dataset/cars.csv', index_col= 0)

# Print out cars
print(cars)
#      cars_per_cap        country  drives_right
# US            809  United States          True
# AUS           731      Australia         False
# JPN           588          Japan         False
# IN             18          India         False
# RU            200         Russia          True
# MOR            70        Morocco          True
# EG             45          Egypt          True