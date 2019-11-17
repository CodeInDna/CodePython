# Comparison of booleans
print(True == False)		#False

# Comparison of integers
print((-5*15) != 75)		#True

# Comparison of strings
print("pyscript" == "PyScript")		#False

# Compare a boolean with an integer
print(True == 1)		#True

# Comparison of integers
x = -3 * 6
print(x >= -10)		# False

# Comparison of strings
y = "test"
print(y >= "test")	#True

# Comparison of booleans
print(True > False)	#True


# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)	#[ True  True False False]

# my_house less than your_house
print(my_house < your_house)	#[False  True  True False]