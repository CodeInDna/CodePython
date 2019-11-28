# $$$$$$$$$$$ Combining rows of data $$$$$$$$$$$$ #
# The dataset we'll be working with here relates to NYC Uber data. The 
# original dataset has all the originating Uber pickup locations by time 
# and latitude and longitude.

# Three DataFrames are there: uber1, which contains data for April 2014, uber2,
# which contains data for May 2014, and uber3, which contains data for June 2014. 
# this exercise is to concatenate these DataFrames together such that 
# the resulting DataFrame has the data for all three months.

import pandas as pd
uber1 = pd.read_csv('dataset/uber1.csv')
uber2 = pd.read_csv('dataset/uber2.csv')
uber3 = pd.read_csv('dataset/uber3.csv')

# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1, uber2, uber3])

# Print the shape of row_concat
print(row_concat.shape)		# (297, 5)

# Print the head of row_concat
print(row_concat.head())
#    Unnamed: 0         Date/Time      Lat      Lon    Base
# 0           0  4/1/2014 0:11:00  40.7690 -73.9549  B02512
# 1           1  4/1/2014 0:17:00  40.7267 -74.0345  B02512

 
 
 # $$$$$$$$$$$ Combining columns of data $$$$$$$$$$$$ #
# Think of column-wise concatenation of data as stitching data together 
# rom the sides instead of the top and bottom. To perform this action, 
# you use the same pd.concat() function, but this time with the keyword 
# gument axis=1. The default, axis=0, is for a row-wise concatenation.
# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola = pd.read_csv('dataset/ebola.csv')
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='status_country', value_name='counts')

country = ebola_melt.status_country.str.split('_').str.get(1)

# Concatenate ebola_melt and country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, country], axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())


# $$$$$$$$$$$ Combining multiple files using pattern $$$$$$$$$$$$ #
# $$$$$$$$$$$ Finding files that match a pattern $$$$$$$$$$$$ #
# You're now going to practice using the glob module to find all csv files in the workspace
# the glob module has a function called glob that takes a pattern and returns a list of the 
# files in the working directory that match that pattern.
# For example, if you know the pattern is part_ single digit number .csv, you can write the 
# pattern as 'part_?.csv' (which would match part_1.csv, part_2.csv, part_3.csv, etc.)
import glob

# Write the pattern: pattern
pattern = 'dataset/uber*.csv'

# Save all file matches: csv_files
csv_files = glob.glob(pattern)

# Print the file names
print(csv_files)

# Load the second file into a DataFrame: csv2
csv2 = pd.read_csv(csv_files[1])

# Print the head of csv2
print(csv2.head())


# $$$$$$$$$$$ Iterating & Concatenating all matches $$$$$$$$$$$$ #
# Now that you have a list of filenames to load, you can load all the files into a list of DataFrames that can then be concatenated.

# You'll start with an empty list called frames. Your job is to use a for loop to:

# iterate through each of the filenames
# read each filename into a DataFrame, and then
# append it to the frames list.
# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

# Print the shape of uber
print(uber.shape)	# (297, 5)

# Print the head of uber
print(uber.head())
print(uber.tail())
   # Unnamed: 0         Date/Time      Lat      Lon    Base
# 0           0  4/1/2014 0:11:00  40.7690 -73.9549  B02512
# 1           1  4/1/2014 0:17:00  40.7267 -74.0345  B02512


# $$$$$$$$$$$ 1-to-1 data merge $$$$$$$$$$$$ #
# Merging data allows you to combine disparate datasets into a single dataset to do more complex analysis.

# Here, we'll be using survey data that contains readings that William Dyer, Frank 
# Pabodie, and Valentina Roerich took in the late 1920s and 1930s while they were on 
# an expedition towards Antarctica. 
site = pd.read_csv('dataset/site.csv')
visited = pd.read_csv('dataset/visited.csv')
# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(o2o)
#    Unnamed: 0_x name_x  lat_x  long_x  Unnamed: 0_y name_y  lat_y  long_y  ident   site       dated
# 0             0   DR-1 -49.85 -128.57             0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
# 1             1   DR-3 -47.15 -126.72             1   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
# 2             2  MSK-4 -48.87 -123.40             2  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14

# $$$$$$$$$$$ Many-to-1 data merge $$$$$$$$$$$$ #
# In a many-to-one (or one-to-many) merge, one of the values will be duplicated and recycled in the output. 
# That is, one of the keys in the merge is not unique.
# Note that this time, visited has multiple entries for the site column.
visited2 = pd.read_csv('dataset/visited2.csv')
# Merge the DataFrames: m2o
m2o = pd.merge(left=site, right=visited2, left_on='name', right_on='site')

# Print m2o
print(m2o)
#    Unnamed: 0_x   name    lat    long  Unnamed: 0_y  ident   site       dated
# 0             0   DR-1 -49.85 -128.57             0    619   DR-1  1927-02-08
# 1             0   DR-1 -49.85 -128.57             1    622   DR-1  1927-02-10
# 2             0   DR-1 -49.85 -128.57             7    844   DR-1  1932-03-22
# 3             1   DR-3 -47.15 -126.72             2    734   DR-3  1939-01-07

# $$$$$$$$$$$ Many-to-Many data merge $$$$$$$$$$$$ #
# The final merging scenario occurs when both DataFrames do not have unique keys for a merge. What happens 
# here is that for each duplicated key, every pairwise combination will be created.
# Here, We'll work with the site and visited DataFrames from before, 
# and a new survey DataFrame. our task is to merge site and visited 
# We will then merge this merged DataFrame with survey.
# Merge site and visited: m2m
survey = pd.read_csv('dataset/survey.csv')
m2m = pd.merge(left=site, right=visited2, left_on='name', right_on='site')

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.head(20))
