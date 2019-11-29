# $$$$$$$$$$$$ Converitng data types $$$$$$$$$$$ #
# NOTE: categorical variables in a DataFrame are of type category reduces memory usage.
import pandas as pd

tips = pd.read_csv('dataset/tips.csv')

# Print the type of tips variables
print(tips.dtypes)
# sex            object
# smoker         object

# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips['smoker'] = tips['smoker'].astype('category')	

# Print the info of tips
print(tips.info())
# sex           244 non-null category
# smoker        244 non-null category
# Notice: By converting sex and smoker to categorical variables, the memory 
# usage of the DataFrame went down from 13.4 KB to 10.1KB. This may seem like 
# a small difference here, but when you're dealing with large datasets,  
# the reduction in memory usage can be very significant!

# $$$$$$$$$$$$ Working with numeric data $$$$$$$$$$$ #
# If you expect the data type of a column to be numeric (int or float), but 
# instead it is of type object, this typically means that there is a non 
# numeric value in the column, which also signifies bad data.
# We can use the pd.to_numeric() function to convert a column into a numeric 
# data type. If the function raises an error, we can be sure that there is a 
# bad value within the column. You can choose to ignore or coerce the value 
# into a missing value, NaN
# The dtype of total_bill and tips are of type object
# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')
# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')
# Print the info of tips
print(tips.info())
# total_bill    202 non-null float64
# tip           220 non-null float64

# Notice: The 'total_bill' and 'tip' columns in this DataFrame are stored as object 
# types because the string 'missing' is used in these columns to encode 
# missing values. By coercing the values into a numeric type, they become 
# proper NaN values.


# $$$$$$$$$$$$ String parsing with regular expressions $$$$$$$$$$$ #
# When working with data, it is sometimes necessary to write a regular 
# expression to look for properly entered values. Phone numbers in a dataset 
# is a common field that needs to be checked for validity.in the below exercise is 
# to define a regular expression to match US phone numbers that fit the 
# pattern of xxx-xxx-xxxx.The regular expression module in python is re. 
# When performing pattern matching on data, since the pattern will be used 
# for a match across multiple rows, it's better to compile the pattern first 
# using re.compile(), and then use the compiled pattern to match values.
# Import the regular expression module
import re

# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))			# True

# See if the pattern matches
result2 = prog.match('1123-456-7890')
print(bool(result2))		# False

# $$$$$$$$$$$$ Extracting numerical values from strings $$$$$$$$$$$ #
# Extracting numbers from strings is a common task, particularly when working 
# with unstructured data or log files.
# Say you have the following string: 'the recipe calls for 6 strawberries and 
# 2 bananas'.
# It would be useful to extract the 6 and the 2 from this string to be saved 
# or later use when comparing strawberry to banana ratios.
# When using a regular expression to extract multiple numbers (or multiple 
# pattern matches, to be exact), you can use the re.findall() function.
# You pass in a pattern and a string to re.findall(), and it will return a list of the matches.
# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)	# ['10', '1']

# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)	# True

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2) # True

# Write the third pattern
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)	# True


# $$$$$$$$$$$$ Custom functions to clean data $$$$$$$$$$$ #
# Tips dataset has a 'sex' column that contains the values 'Male' or 'Female'. Your 
# job is to write a function that will recode 'Female' to 0, 'Male' to 1, 
# and return np.nan for all entries of 'sex' that are neither 'Female' nor 
# 'Male'.
import numpy as np
# Define recode_gender()
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0
    
    # Return 1 if gender is 'Male'    
    elif gender == 'Male':
        return 1
    
    # Return np.nan    
    else:
        return np.nan

# Apply the function to the sex column
tips['recode'] = tips.sex.apply(recode_gender)

# Print the first five rows of tips
print(tips.head())
#    total_bill   tip     sex smoker  day    time  size recode
# 0       16.99  1.01  Female     No  Sun  Dinner     2      0
# 1       10.34  1.66    Male     No  Sun  Dinner     3      1


# $$$$$$$$$$$$ Lambda functions $$$$$$$$$$$ #
# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall("\d+\.\d+", x)[0])

# Print the head of tips
print(tips.head())


# $$$$$$$$$$$$ Dropping duplicate data $$$$$$$$$$$ #
# Duplicate data causes a variety of problems. From the point of view of 
# performance, they use up unnecessary amounts of memory and cause unneeded 
# calculations to be performed when processing data. In addition, they can 
# also bias any analysis results.
billboard = pd.read_csv('dataset/billboard.csv')

# Create the new DataFrame: tracks
tracks = billboard[['year','artist','track','time']]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())
# After dropping duplicates, the DataFrame has gone from having 24092 entries to only 317!

# $$$$$$$$$$$$ Filling missing data $$$$$$$$$$$ #
# It's rare to have a (real-world) dataset without any missing values, and 
# it's important to deal with them because certain calculations cannot handle 
# missing values while some calculations will, by default, skip over any 
# missing values.
airquality = pd.read_csv('dataset/airquality.csv')

# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)

# Print the info of airquality
print(airquality.info())
# RangeIndex: 153 entries, 0 to 152
# Data columns (total 6 columns):
# Ozone      153 non-null float64

# $$$$$$$$$$$$ Testing your data with asserts $$$$$$$$$$$ #
# DataFrame method to check for missing values in a column. The .all() method 
# returns True if all values are True. When used on a DataFrame, it returns a 
# Series of Booleans - one for each column in the DataFrame. So if you are 
# using it on a DataFrame, like in this exercise, you need to chain another 
# .all() method so that you return only one True or False value. When using 
# these within an assert statement, nothing will be returned if the assert 
# statement is true: This is how you can confirm that the data you are checking 
# are valid.The first .all() method will return a True or False for each column, 
# while the second .all() method will return a single True or False.
ebola = pd.read_csv('dataset/ebola.csv')
# Assert that there are no missing values
# assert pd.notnull(ebola).all().all()

# Assert that all values are >= 0
# assert (ebola >= 0).all().all()


# $$$$$$$$$$$$ Exploratory analysis $$$$$$$$$$$ #
# Here, the goal is to visually check the data for insights as well as errors. 
# When looking at the plot, pay attention to whether the scatter plot takes 
# the form of a diagonal line, and which points fall below or above the 
# diagonal line. This will inform how life expectancy in 1899 changed (or did 
# 	not change) compared to 1800 for different countries. If points fall on a 
# diagonal line, it means that life expectancy remained the same!
g1800s = pd.read_csv('dataset/g1800s.csv')
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()
