# flat files - .txt or .csv
# The Most Basic importing technique
file = open("dataset/moby_dick.txt", 'r')
# print(file.read())
file.close()

file = open("dataset/cars.csv", 'r')
# print(file.read())
file.close()

# The Intermediate Approach
with open("dataset/moby_dick.txt") as file:
	d = file.read()
# print(d)

with open("dataset/cars.csv") as file:
	d = file.readline()
# print(d)

# The Standard Approach (Using numpy)
# loadtxt(): (Only numerical data allowed)
import numpy as np
data = np.loadtxt("dataset/digits.csv", delimiter=',')
# print(data)

data = np.loadtxt("dataset/seaslug.txt", delimiter='\t', dtype=str)
# print(data[0])

data_float = np.loadtxt("dataset/seaslug.txt", delimiter='\t', dtype=float, skiprows=1)
# print(data_float)

data_all_types = np.genfromtxt("dataset/titanic.csv", delimiter=',', dtype=None, names=True)
# data_all_types = np.recfromcsv("dataset/titanic.csv")
# print(data_all_types[:3])

# The Standard Approach (Using pandas)
import pandas as pd
data = pd.read_csv("dataset/titanic.csv",nrows=5, na_values='Nothing')
# print(data.head())

# data_array = np.array(data)
# print(data)


# Excel Files
import pandas as pd
file = "dataset/battledeath.xlsx"
data = pd.ExcelFile(file)
# print(data.sheet_names)

# data1 = data.parse('2004')
# data1 = data.parse(1)
data1 = data.parse(1, usecols=[1], skiprows=[], names=['Year'])
# print(data1.head())

# SAS Files
from sas7bdat import SAS7BDAT
with SAS7BDAT("dataset/sales.sas7bdat") as file:
	d = file.to_data_frame()
# print(d.head())


# Stata Files
import pandas as pd
data = pd.read_stata("dataset/disarea.dta")
# print(data.head())


# HDf5
import h5py
data = h5py.File("dataset/LIGO_data.hdf5", 'r')
print(data.keys())
for key in data['meta'].keys():
	print(key)
print(data['meta']['Detector'].value)


# Mat files
import scipy.io
mat = scipy.io.loadmat('dataset/ja_data2.mat')
print(mat.keys())