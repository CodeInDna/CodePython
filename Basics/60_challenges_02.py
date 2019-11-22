print("CHALLENGE 01 starts here*****************")
# Create a function sum_up_diagonals which accepts an N*N list of lists and sums
# the two main diagonals in the array: the one from the upper left to the lower
# right, and one from upper right to lower left.

def sum_up_diagonals(list):
	sum_dig = 0
	for index, val in enumerate(list):
		sum_dig += list[index][index]
		sum_dig += list[index][-1-index]
	return sum_dig
list1 = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
list2 = [
	[4,1,0],
	[-1,-1,0],
	[0,0,9]
]
print(sum_up_diagonals(list1))	# 30
print(sum_up_diagonals(list2))	# 11

print("CHALLENGE 01 ends here*****************")



print("CHALLENGE 02 starts here*****************")
# Create a function min_max_key_in_dictionary which returns a list with the lowest key in the
# dictionary and the highest key in the dict. You can assume that the dict will have keys that
# are numbers.

def min_max_key_in_dictionary(dictionary):
	keys = dictionary.keys()
	return [min(keys), max(keys)]
dict1 = {2:'a',7:'b',1:'c',10:'d',4:'e'}
print(min_max_key_in_dictionary(dict1))		# [1, 10]

print("CHALLENGE 02 ends here*****************")




print("CHALLENGE 03 starts here*****************")
# Create a function find_greater_number which accepts a list and returns the number of times a
# number is followed by a larger number across the entire list.
def find_greater_number(lst):
	count = 0
	for i in range(1, len(lst)):
		for j in range(0, i):
			if lst[i] > lst[j]:
				count += 1
	return count
print(find_greater_number([1,2,3]))			# 3
print(find_greater_number([6,1,2,7]))		# 4
print(find_greater_number([5,4,3,2,1]))		# 0

print("CHALLENGE 03 ends here*****************")




print("CHALLENGE 04 starts here*****************")
# Create a function two_oldest which accepts a list of numbers as its arguments and returns two highest 
# numbers within the list. The returnes value should be a list in the format [second oldest age, oldest age]
def two_oldest(lst):
	return sorted(lst)[-2:]
print(two_oldest([1,2,10,8]))			# [8, 10]
print(two_oldest([6,1,9,10,7]))			# [9, 10]
print(two_oldest([4,35,25,29,10,54]))	# [35, 54]

print("CHALLENGE 04 ends here*****************")




print("CHALLENGE 05 starts here*****************")
# Create a function is_odd_string which accepts a string and returns true is sum of each character's position 
# in the alphabet is odd. If the sum is even, return False. NOTE: indexing starts at 1
from functools import reduce
def is_odd_string(string):
	sum_str = sum(ord(a)-96 for a in string.lower()) or 0
	return sum_str % 2 != 0
print(is_odd_string('a'))			# True
print(is_odd_string('aaaa'))		# False
print(is_odd_string('amazing'))	    # True
print(is_odd_string('veryfunny'))	# False

print("CHALLENGE 05 ends here*****************")

