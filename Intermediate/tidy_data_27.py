# $$$$$$$$$$$ Tidy Data $$$$$$$$$$$ 

# $$$$$$$$$ Principles of tidy data $$$$$$$$$$
# * Colums represent separate variables
# * Rows represent individual observations
# * Observational units form tables

# $$$$$$$$$ Converting to tidy data $$$$$$$$$$
# The data problem we are trying to fix:
	# Columns containing values, instead of variables 
# Solution : pld.melt()

# $$$$$$$$$ Reshaping your data using melt $$$$$$$$$$
# Melting data is the process of turning columns of your data 
# into rows of data. Consider the DataFrames from the previous 
# exercise. In the tidy DataFrame, the variables Ozone, Solar.R, 
# Wind, and Temp each had their own column. If, however, you 
# wanted these variables to be in rows instead, you could melt 
# the DataFrame. In doing so, however, you would make the data 
# untidy! This is important to keep in mind: Depending on how 
# your data is represented, you will have to reshape it differently 
# (e.g., this could make it easier to plot values).

# There are two parameters you should be aware of: id_vars and 
# value_vars. The id_vars represent the columns of the data you 
# do not want to melt (i.e., keep it in its current shape), while 
# the value_vars represent the columns you do wish to melt into 
# rows. By default, if no value_vars are provided, all columns 
# not set in the id_vars will be melted. This could save a bit of 
# typing, depending on the number of columns that need to be 
# melted.
import pandas as pd 

airquality = pd.read_csv('dataset/airquality.csv')

# Print the head of airquality
print(airquality.head())
#    Ozone  Solar.R  Wind  Temp  Month  Day
# 0   41.0    190.0   7.4    67      5    1
# 1   36.0    118.0   8.0    72      5    2
# ...so on

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality,id_vars=['Month','Day'], value_vars=['Ozone','Solar.R','Wind','Temp'])

# Print the head of airquality_melt
print(airquality_melt.head())
#    Month  Day variable  value
# 0      5    1    Ozone   41.0
# 1      5    2    Ozone   36.0
# ....so on

# $$$$$$$$$ Customizing melted data $$$$$$$$$$
# When melting DataFrames, it would be better to have column names 
# more meaningful than variable and value (the default names used 
# by pd.melt()).You can rename the variable column by specifying an 
# argument to the var_name parameter, and the value column by 
# specifying an argument to the value_name parameter.

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'], value_vars=['Ozone','Solar.R','Wind','Temp'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())
#    Month  Day measurement  reading
# 0      5    1       Ozone     41.0
# 1      5    2       Ozone     36.0

# $$$$$$$$$ pivot(): un-melting data $$$$$$$$$$
	# Opposite of melting
	# In melting: we turned columns into rows
	# Pivoting: turn unique values into separate columns

# $$$$$$$$$ Pivot data $$$$$$$$$$
# Pivoting data is the opposite of melting it. Remember the tidy 
# form that the airquality DataFrame was in before you melted it?
# While melting takes a set of columns and turns it into a single 
# column, pivoting will create a new column for each unique value 
# in a specified column.
# .pivot_table() has an index parameter which you can use to 
# specify the columns that you don't want pivoted: It is similar to 
# the id_vars parameter of pd.melt(). Two other parameters that 
# you have to specify are columns (the name of the column you 
# want to pivot), and values (the values to be used when the 
# column is pivoted).
# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month','Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())
# measurement  Ozone  Solar.R  Temp  Wind
# Month Day
# 5     1       41.0    190.0  67.0   7.4
#       2       36.0    118.0  72.0   8.0
# Notice: pivoted DataFrame does not actually look like the original DataFrame. 

# $$$$$$$$$ Resetting the index of a DataFrame $$$$$$$$$$
# After pivoting airquality_melt in the previous exercise, you didn't quite get back the original DataFrame.
# What you got back instead was a pandas DataFrame with a hierarchical index (also known as a MultiIndex).
# Hierarchical indexes are covered in depth in Manipulating DataFrames with pandas. In essence, they allow 
# you to group columns or rows by another variable - in this case, by 'Month' as well as 'Day'.
# There's a very simple method you can use to get back the original DataFrame from the pivoted DataFrame: .reset_index().
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()

# Print the new index of airquality_pivot_reset
print(airquality_pivot_reset.index)

# Print the head of airquality_pivot_reset
print(airquality_pivot_reset.head())
# measurement  Month  Day  Ozone  Solar.R  Temp  Wind
# 0                5    1   41.0    190.0  67.0   7.4
# 1                5    2   36.0    118.0  72.0   8.0

# $$$$$$$$$ Pivoting duplicate values $$$$$$$$$$
# You can also use pivot tables to deal with duplicate values by providing an 
# aggregation function through the aggfunc parameter.
# Let's say your data collection method accidentally duplicated your dataset as airquality_dup
# You'll see that by using .pivot_table() and the aggfunc parameter, you can 
# not only reshape your data, but also remove duplicates. Finally, you can then flatten the 
# columns of the pivoted DataFrame using .reset_index().
import numpy as np

airquality_dup = pd.read_csv('dataset/airquality_dup.csv')

# print(airquality.shape)	# (153, 6)
# print(airquality_dup.shape)	# (165, 6)	Duplicate rows present

# Pivot table the airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=['Month','Day'], columns='measurement', values='reading', aggfunc=np.mean)

# Print the head of airquality_pivot before reset_index
print(airquality_pivot.head())
# measurement  Ozone  Solar.R  Temp  Wind
# Month Day                              
# 5     1       41.0    190.0  67.0   7.4
#       2       36.0    118.0  72.0   8.0

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())
# measurement  Month  Day  Ozone  Solar.R  Temp  Wind
# 0                5    1   41.0    190.0  67.0   7.4
# 1                5    2   36.0    118.0  72.0   8.0

# Print the head of airquality
print(airquality.head())
# 	measurement  Month  Day  Ozone  Solar.R  Temp  Wind
#     0                5    1   41.0    190.0  67.0   7.4
#     1                5    2   36.0    118.0  72.0   8.0


# $$$$$$$$$ Splitting a column with .str $$$$$$$$$$
# This dataset consisting of case counts of tuberculosis by country, year, 
# gender, and age group. you're going to tidy the 'm014' column, which 
# represents males aged 0-14 years of age. In order to parse this value, you 
# need to extract the first letter into a new column for gender, and the rest 
# into a column for age_group. Here, since you can parse values by position, 
# you can take advantage of pandas' vectorized string slicing by using the 
# str attribute of columns of type object.
tb = pd.read_csv('dataset/tb.csv')

# Melt tb: tb_melt
tb_melt = pd.melt(frame=tb, id_vars=['country', 'year'])

# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:]

# Print the head of tb_melt
print(tb_melt.head())
#   country  year variable  value gender age_group
# 0      AD  2000     m014    0.0      m       014
# 1      AE  2000     m014    2.0      m       014

# $$$$$$$$$ Splitting a column with .split() and a .get() $$$$$$$$$$
# Notice that the data has column names such as Cases_Guinea and Deaths_Guinea. 
# Here, the underscore _ serves as a delimiter between the first part (cases or 
# deaths), and the second part (country).
# This time, you cannot directly slice the variable by position as in the 
# previous exercise. You now need to use Python's built-in string method 
# called .split(). By default, this method will split a string into parts 
# separated by a space. However, in this case you want it to split by an 
# underscore. You can do this on 'Cases_Guinea', for example, using 
# 'Cases_Guinea'.split('_'), which returns the list ['Cases', 'Guinea'].
ebola = pd.read_csv('dataset/ebola.csv')

# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())
         # Date  Day  type_country  counts        str_split   type country
# 0    1/5/2015  289  Cases_Guinea  2776.0  [Cases, Guinea]  Cases  Guinea
# 1    1/4/2015  288  Cases_Guinea  2775.0  [Cases, Guinea]  Cases  Guinea
