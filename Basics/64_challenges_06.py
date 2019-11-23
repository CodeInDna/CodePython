print("CHALLENGE 01 starts here*****************")
# Create a function two_list_dictionary which accepts two list of varying length. The first list consists of
# values. Your fn should return a dict created from the keys and values. If there are not enough values, the 
# remaining keys should have a value of null. If there are not enough keys, just ignore the remaining values

def two_list_dictionary(list1, list2):
	collection = {}
	for idx, key in enumerate(list1):
		if idx < len(list2):
			collection[list1[idx]] = list2[idx]
		else:
			collection[list1[idx]] = None
	return collection
print(two_list_dictionary(['a','b','c','d'], [1,2,3]))	# {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a','b','c'], [1,2,3,4]))	# {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x','y','z'], [1,2]))		# {'x': 1, 'y': 2, 'z': None}
print("CHALLENGE 01 ends here*****************")



print("CHALLENGE 02 starts here*****************")
# Create a function range_in_list which accepts a list and start and end indices returns the sum of the values between
# and including the start and end index. If the start parameter is not passed in, it should defaul to zero.
# Also, if the end argument is too large, the sum should still go through the end of the list.
# def range_in_list(lst, start=0, end=None):
# 	if not start: start = 0
# 	if not end or end >= len(lst): end = len(lst)-1
# 	sum = 0
# 	for i in range(start, end+1):
# 		sum += lst[i]
# 	return sum
# or
def range_in_list(lst, start=0, end=None):
	end = end or lst[-1]
	return sum(lst[start:end+1])
print(range_in_list([1,2,3,4],0,2))		# 6
print(range_in_list([1,2,3,4],0,3))		# 10
print(range_in_list([1,2,3,4],1))		# 9
print(range_in_list([1,2,3,4]))			# 10
print(range_in_list([1,2,3,4],0,100))	# 10
print(range_in_list([],0,1))			# 0
print("CHALLENGE 02 ends here*****************")


print("CHALLENGE 03 starts here*****************")
# Create a function same_frequency which accepts two numbers and returns True
# If they contain the same frequency of digits. Otherwise it returns False
def same_frequency(num1, num2):
	count_num1 = {letter: str(num1).count(letter) for letter in str(num1)}
	count_num2 = {letter: str(num2).count(letter) for letter in str(num2)}

	for key,val in count_num1.items():
		if not key in count_num2.keys():
			return False
		elif count_num2[key] != count_num1[key]:
			return False
	return True
print(same_frequency(551122, 221515))			# True
print(same_frequency(321142, 3212215))			# False
print(same_frequency(1212, 2211))				# True
print("CHALLENGE 03 ends here*****************")


print("CHALLENGE 04 starts here*****************")
# Create a function nth which accepts a list and a numbers and returns the element at whatever index is the number
# in the list. If the number is negative, the nth element from the end is returned
def nth(lst, idx):
	if idx >= 0:
		return lst[idx]
	return lst[len(lst) + idx]
print(nth(['a','b','c','d'], 1))			# b
print(nth(['a','b','c','d'], -2))			# c
print(nth(['a','b','c','d'], 0))			# a
print(nth(['a','b','c','d'], -4))			# a
print(nth(['a','b','c','d'], -1))			# d
print(nth(['a','b','c','d'], 3))			# d
print("CHALLENGE 04 ends here*****************")


print("CHALLENGE 05 starts here*****************")
# Create a function find_the_duplicate which accepts an array of numbers containing a single duplicate.
# The fn returns the number which is a duplicate or None if there are no duplicates.
def find_the_duplicate(lst):
	new_lst = []
	for num in lst:
		if num in new_lst:
			return num
		else:
			new_lst.append(num)
	return None
print(find_the_duplicate([1,2,1,4,3,12]))			# 1
print(find_the_duplicate([6,1,9,5,3,4,9],))			# 9
print(find_the_duplicate([2,1,3,4]))			    # None
print("CHALLENGE 05 ends here*****************")

