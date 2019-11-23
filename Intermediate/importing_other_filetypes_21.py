# Importing other file types
# Excel spreadsheets
# MATLAB files
# SAS files
# Stata files
# HDF5 files

# ls is used to explore your current working directory. You can also do 
# this natively in Python using the library os, which consists of 
# miscellaneous operating system interfaces.
import os 
wd = os.getcwd()
# print(os.listdir(wd))	# list all the directories in current wd
# The first line of the following code imports the library os, 
# the second line stores the name of the current directory in a string 
# called wd and the third outputs the contents of the directory in a 
# list to the shell.
# .xlsx is not a flat because it is a spreadsheet consisting of many sheets, not a single table.


# Loading a pickled file***************************************
# There are a number of datatypes that cannot be saved easily to flat 
# files, such as lists and dictionaries. If you want your files to be 
# human readable, you may want to save them as text files in a clever 
# manner. JSONs are appropriate for Python dictionaries.
# However, if you merely want to be able to import them into Python, 
# you can serialize them. All this means is converting the object into 
# a sequence of bytes, or a bytestream.

# Import pickle package
import pickle 

# Open pickle file and load data: d
# with open('dataset/pets.pkl', 'rb') as file:
    # d = pickle.load(file)

# Print d
# print(d)

# Print datatype of d
# print(type(d))

# Listing sheets in Excel files***********************************
# Whether you like it or not, any working data scientist will 
# need to deal with Excel spreadsheets at some point in time. You won't always want to do so in Excel, however!
# We use pandas to import excel spreadsheets. you can retrieve a 
# list of the sheet names using the attribute spreadsheet.sheet_names
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'dataset/battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)	# ['2002', '2004']

# importing sheets from excel file 
# We can access sheets by passing sheet name or index
df1 = xls.parse('2004')
print(df1.head())

df2 = xls.parse(0)
print(df2.head())



# Customizing your spreadsheet import
# Here, you'll parse your spreadsheets and use additional arguments 
# to skip rows, rename columns and select only particular columns.
# Parse the first sheet and rename the columns: df1
df3 = xls.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df3.head())

# Parse the first column of the second sheet and rename the column: df2
df4 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df4.head())


# Importing DAS/Stata files using pandas
# SAS: Statistical Analysis System
# Stata: Statistics + Data
# SAS: business analytics and biostatistics
# Stata: academic social sciences research
# SAS files used for:
# Advanced analytics
# Multivariate analysis
# Business Intelligence
# Data anagement
# Predictive analysis
# Standard for computational analysis

# Importing SAS files
from sas7bdat import SAS7BDAT

with SAS7BDAT("dataset/sales.sas7bdat") as file:
	df_sas = file.to_data_frame()
print(df_sas.head())

# Importing Stata files
# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('dataset/disarea.dta')

# Print the head of the DataFrame df
print(df.head())


# sing h5py to import HDF5 files(Heirarchical Data Format)
# Used to store and organize large amount of data
import h5py

# Assign filename: file
file = 'dataset/LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))
# <class 'h5py._hl.files.File'>

# Print the keys of the file
for key in data.keys():
    print(key)
# meta
# quality
# strain

# Extracting data from your HDF5 file
# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)	# Strain

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value
print(strain)	# [-1.77955839e-18 -1.76552067e-18 -1.71049117e-18 ... -1.76375155e-18
 # -1.72364846e-18 -1.71969299e-18]


 # Importing MATLAB files
 # Matrix Laboratory
 # Industry standard in engg and science
 # Data saved in .mat files
 # keys of dict = MATLAB variable names
 # values of dict = objects assigned to variables

# Loading .mat files
import scipy.io
import numpy as np
# Load MATLAB file:
mat = scipy.io.loadmat('dataset/ja_data2.mat')

# Print the datatype of mat 
print(type(mat))	# <class 'dict'>

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))	#<class 'numpy.ndarray'>

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))	#(200, 137)

# Subset the array and plot it
# data = mat['CYratioCyt'][25, 5:]
# fig = plt.figure()
# plt.plot(data)
# plt.xlabel('time (min.)')
# plt.ylabel('normalized fluorescence (measure of expression)')
# plt.show()
