# Import cars data
import pandas as pd
cars = pd.read_csv('dataset/cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]
# US      True
# AUS    False
# JPN    False
# IN     False
# RU      True
# MOR     True
# EG      True
# Name: drives_right, dtype: bool

# Use dr to subset cars: sel
sel = cars[dr]
# OR
# Convert code to a one-liner
# sel = cars[cars['drives_right']]

# Print sel
print(sel)
#      cars_per_cap        country  drives_right
# US            809  United States          True
# RU            200         Russia          True
# MOR            70        Morocco          True
# EG             45          Egypt          True


# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)
#      cars_per_cap        country  drives_right
# US            809  United States          True
# AUS           731      Australia         False
# JAP           588          Japan         False

import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)]

# Print medium
print(medium)
#      cars_per_cap        country  drives_right
# US            809  United States          True
# AUS           731      Australia         False
# JAP           588          Japan         False