# $$$$$$$$$$$$$$ Numpy and pandas working together $$$$$$$$$$$$$$$$
# Pandas depends upon and interoperates with NumPy, the Python library for 
# fast numeric array computations. For example, you can use the DataFrame 
# attribute .values to represent a DataFrame df as a NumPy array. You can 
# also pass pandas data structures to NumPy methods. 
import pandas as pd
import numpy as np

df = pd.read_csv('dataset/world_population.csv')

# Create array of DataFrame values: np_vals
np_vals = df.values

# Create new array of base 10 logarithm values: np_vals_log10
np_vals_log10 = np.log10(np_vals)

# Create array of new DataFrame by passing df to np.log10(): df_log10
df_log10 = np.log10(df)

# Print original and new data containers
[print(x, 'has type', type(eval(x))) for x in ['np_vals', 'np_vals_log10', 'df', 'df_log10']]
# np_vals has type <class 'numpy.ndarray'>
# np_vals_log10 has type <class 'numpy.ndarray'>
# df has type <class 'pandas.core.frame.DataFrame'>
# df_log10 has type <class 'pandas.core.frame.DataFrame'>


# $$$$$$$$$$$$$$ Zip lists to build a DataFrame $$$$$$$$$$$$$$$$
# DataFrame of the top three countries to win gold medals since 1896 by first 
# building a dictionary. list_keys contains the column names 'Country' and 'Total'. 
# list_values contains the full names of each country and the number of gold medals 
# awarded. 
list_keys = ['Country', 'Total']
list_values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]

# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)
#           Country  Total
# 0   United States   1118
# 1    Soviet Union    473
# 2  United Kingdom    273

# $$$$$$$$$$$$$$ Lableing your Data $$$$$$$$$$$$$$$$
# You can use the DataFrame attribute df.columns to view and assign new string labels to columns 
# in a pandas DataFrame.
df1 = pd.DataFrame({'a':[1980, 1981, 1982 ], 'b':['Blondie','Christopher Cross','Joan Jett'],
	'c': ['Call Me', 'Arthur\'s Theme', 'I Love Rock and Roll'], 'd': [6,3,7]}) 

# Build a list of labels: list_labels
list_labels = ['year', 'artist', 'song', 'chart weeks']

# Assign the list of labels to the columns attribute: df.columns
df1.columns = list_labels
print(df1)
#    year             artist                  song  chart weeks
# 0  1980            Blondie               Call Me            6
# 1  1981  Christopher Cross        Arthur's Theme            3
# 2  1982          Joan Jett  I Love Rock and Roll            7

# $$$$$$$$$$$$$$ Building DataFrames with broadcasting $$$$$$$$$$$$$$$$
# You can implicitly use 'broadcasting', a feature of NumPy, when creating pandas 
# DataFrames. In this exercise, you're going to create a DataFrame of cities in 
# Pennsylvania that contains the city name in one column and the state name in the 
# second.
cities = ['Manheim','Preston park','Biglerville','Indiana','Curwensville','Crown','Harveys lake','Mineral springs','Cassville','Hannastown','Saltsburg','Tunkhannock','Pittsburgh','Lemasters','Great bend']
# Make a string with the value 'PA': state
state = 'PA'

# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
#    state             city
# 0     PA          Manheim
# 1     PA     Preston park
# 2     PA      Biglerville
# 3     PA          Indiana
# ....so on

# $$$$$$$$$$$$$$ Reading a flat file $$$$$$$$$$$$$$$$
file_path = 'dataset/world_population.csv'
df2 = pd.read_csv(file_path)

# Create a list of the new column labels: new_labels
new_labels = ['year', 'population']

# Read in the file, specifying the header and names parameters: df3
df3 = pd.read_csv(file_path, header=0, names=new_labels)

# Print both the DataFrames
print(df2)
print(df3)


# $$$$$$$$$$$$$$ Delimiters, headers, and extensions $$$$$$$$$$$$$$$$
# The file has three aspects that may cause trouble for lesser tools: 
# multiple header lines, comment records (rows) interleaved throughout 
# the data rows, and space delimiters instead of commas.
file_messy = 'dataset/file_messy.txt'
# Read the raw file as-is: df1
df1 = pd.read_csv(file_messy)

# Print the output of df1.head()
print(df1.head())

# Read in the file with the correct parameters: df2
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head())

file_clean = 'dataset/file_clean.csv'
# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv(file_clean, index=False)

# Save the cleaned up DataFrame to an excel file without the index
df2.to_excel('dataset/file_clean.xlsx', index=False)


# $$$$$$$$$$$$$$ Plotting series using pandas $$$$$$$$$$$$$$$$
import matplotlib.pyplot as plt
# Create a plot with color='red'
df = pd.read_csv('dataset/temp.csv')
df.plot(color='red')

# Add a title
plt.title('Temperature in Austin')

# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()

# $$$$$$$$$$$$$$ Plotting DataFrame $$$$$$$$$$$$$$$$
# Comparing data from several columns can be very illuminating. 
# Pandas makes doing so easy with multi-column DataFrames. By default, 
# calling df.plot() will cause pandas to over-plot all column data, 
# with each column as a single line. 
# we have pre-loaded three columns of data from a weather data set - 
# temperature, dew point, and pressure - but the problem is that 
# pressure has different units of measure. The pressure data, measured 
# in Atmospheres, has a different vertical scaling than that of the 
# other two data columns, which are both measured in degrees Fahrenheit
df = pd.read_csv('dataset/weather_data_austin_2010.csv')
# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['DewPoint']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature','DewPoint']
df[column_list2].plot()
plt.show()
