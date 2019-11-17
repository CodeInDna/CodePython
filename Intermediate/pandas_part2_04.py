# Accessing column and rows using pandas

# Using Square brackets
	# Column Access: brics[["country","capital"]]
	# Row Access: brics[1:4]

# loc (label-based)
	# Row Access: brics.loc[["RU","IN","CH"]]
	# Column Access: brics.loc[:, ["country","capital"]]
	# Row and Column Access: brics.loc[["RU","IN","CH"], ["country","capital"]]

# iloc (Index Based)
	# Row Access: brics.loc[[1,2,3]]
	# Column Access: brics.loc[:, [1,2]]
	# Row and Column Access: brics.loc[[1,2,3], [1,2"]]

# NOTE: The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame.
import pandas as pd
cars = pd.read_csv("dataset/cars.csv", index_col=0)

# SQUARE BRACKETS(Accessing Columns)*****************
# Print out country column as Pandas Series
print(cars['country'])
# US     United States
# AUS        Australia
# JPN            Japan
# IN             India
# RU            Russia
# MOR          Morocco
# EG             Egypt
# Name: country, dtype: object---------Series

# Print out country column as Pandas DataFrame
print(cars[['country']])
#  			country
# US   United States
# AUS      Australia
# JPN          Japan
# IN           India
# RU          Russia
# MOR        Morocco
# EG           Egypt

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])
#            country  drives_right
# US   United States          True
# AUS      Australia         False
# JPN          Japan         False
# IN           India         False
# RU          Russia          True
# MOR        Morocco          True
# EG           Egypt          True

# SQUARE BRACKETS(Accessing Rows)*****************
# Print out first 3 observations
print(cars[0:4])
#      cars_per_cap        country  drives_right
# US            809  United States          True
# AUS           731      Australia         False
# JAP           588          Japan         False
# IN             18          India         False

# Print out fourth, fifth and sixth observation
print(cars[3:6])   
#      cars_per_cap  country  drives_right
# IN             18    India         False
# RU            200   Russia          True
# MOR            70  Morocco          True

# lOC (label based Accessing Rows and Columns)
# Rows
# Print out observation for Japan(Print Series)
print(cars.loc["JAP"])
# cars_per_cap      588
# country         Japan
# drives_right    False
# Name: JAP, dtype: object

# Print out observations for Australia and Egypt(Print DataFrame)
print(cars.loc[["AUS", "EG"]])
#      cars_per_cap    country  drives_right
# AUS           731  Australia         False
# EG             45      Egypt          True

# Rows along with Columns
# Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
print(cars.iloc[5, 2])	#True

# Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
print(cars.iloc[[4,5],[1,2]])
#      country  drives_right
# RU    Russia          True
# MOR  Morocco          True

# Print out drives_right column as Series
print(cars.iloc[:, 2])
# US      True
# AUS    False
# JPN    False
# IN     False
# RU      True
# MOR     True
# EG      True
# Name: drives_right, dtype: bool

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])
#      drives_right
# US           True
# AUS         False
# JPN         False
# IN          False
# RU           True
# MOR          True
# EG           True

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ["cars_per_cap","drives_right"]])
#      cars_per_cap  drives_right
# US            809          True
# AUS           731         False
# JPN           588         False
# IN             18         False
# RU            200          True
# MOR            70          True
# EG             45          True