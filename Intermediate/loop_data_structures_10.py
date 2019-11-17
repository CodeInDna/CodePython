# Dictionary
	# for key, val in my_dict.items():

# Numpy array
	# for val in np.nditer(my_array):

# Dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, val in europe.items():
    print("the capital of "+key+ " is "+val)
# the capital of spain is madrid
# the capital of italy is rome
# the capital of france is paris
# the capital of poland is warsaw
# the capital of germany is berlin
# the capital of austria is vienna
# the capital of norway is oslo


import pandas as pd
cars = pd.read_csv("dataset/cars.csv", index_col=0)

# for label, row in cars.iterrows():
# 	print(label)
# 	print(row)
# US
# cars_per_cap              809
# country         United States
# drives_right             True
# Name: US, dtype: object ...so on till end

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab)+": "+str(row['cars_per_cap']))
# 0: 809
# 1: 731
# 2: 588
# 3: 18
# 4: 200
# 5: 70
# 6: 45


# for adding column in the dataset
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
print(cars)
#      cars_per_cap        country  drives_right        COUNTRY
# US            809  United States          True  UNITED STATES
# AUS           731      Australia         False      AUSTRALIA
# JAP           588          Japan         False          JAPAN
# IN             18          India         False          INDIA
# RU            200         Russia          True         RUSSIA
# MOR            70        Morocco          True        MOROCCO
# EG             45          Egypt          True          EGYPT

# Use .apply(str.upper) to do the same thing as above
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)