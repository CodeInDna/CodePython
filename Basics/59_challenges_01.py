# ***********************Let the CHALLENGES begin**********************

print("CHALLENGE 01 starts here*****************")
# Create a function running_average that returns a function. When the fn returned
# is passed a value, the fn returns the current avg of all previous fn calls. You 
# will have to use closure to solve this problem. You should round all answers to the 
# 2nd deciaml place.

def running_average():
	all_args = []
	def sample_fn(num):
		all_args.append(num)
		avg = sum(all_args)/len(all_args)
		return avg
	return sample_fn

rAvg = running_average()
print(rAvg(10))	# 10.0
print(rAvg(11))	# 10.5
print(rAvg(12))	# 11.0

rAvg2 = running_average()
print(rAvg2(1))	# 1.0
print(rAvg2(3))	# 2.0

print("CHALLENGE 01 ends here*****************")

print("CHALLENGE 02 starts here*****************")
# Create a function titlesize which accepts a string of words and return a new string 
# with the first letter of every word in the string capitalized. 

def titlesize(str):
	return ' '.join([word[0].upper() + word[1:] for word in str.split(" ")])
print(titlesize("this is awesome"))				#This Is Awesome
print(titlesize("oNLY cAPITALIZe firST"))		#ONLY CAPITALIZe FirST

print("CHALLENGE 02 ends here*****************")

print("CHALLENGE 03 starts here*****************")
# Create a function find_factors which accepts a number and returns a list of all of the 
# numbers which are divisible by starting from 1 and going up to the number 

def find_factors(num):
	return [n for n in range(1, num + 1) if num % n == 0]
print(find_factors(11))		# [1, 11]		
print(find_factors(12))		# [1, 2, 3, 4, 6, 12]		
print(find_factors(111))	# [1, 3, 37, 111]			
print(find_factors(321421))	# [1, 293, 1097, 321421]			

print("CHALLENGE 03 ends here*****************")

print("CHALLENGE 04 starts here*****************")
# Create a function includes which accepts a collection, a value and an optional starting index.
# The function should return True if the value exists in the collection when we search starting from the starting index
# Otherwise, it should return False. The collection can be a string, a list, or a dict. If the collection
# is a string or array, the third param is starting index for where to search from. If the collection is
# a dict, the fn searches for the value among values in the dict; since objects have no sort order, the
# third param is ignored

def includes(coll, to_search, starting_ind = None):
	if type(coll) == dict:
		return to_search in coll.items()
	if starting_ind is None:
		return to_search in coll
	return to_search in coll[starting_ind:]
print(includes([1, 2, 3], 1))			 # True	
print(includes([1, 2, 3], 1, 2))		 # False		
print(includes({'a':1, 'b':2}, 1))		 # False		
print(includes({'a':1, 'b':2}, 'a'))	 # False		
print(includes('abcd', 'b'))			 # True	
print(includes('abcd', 'e'))			 # False	

print("CHALLENGE 04 ends here*****************")

print("CHALLENGE 05 starts here*****************")
# Create a function repeat which accepts a string and a number and returns a new string passed to the fn
# repeated the number of amount of times. Do not use built-in repeat method 

def repeat(string, num):
	return string * num	
print(repeat('*', 3))	# ***
print(repeat('abc', 2))	# abcabc
print(repeat('abc', 0))	# 
print("CHALLENGE 05 ends here*****************")

print("CHALLENGE 06 starts here*****************")
# Create a function truncate that will shorten a string to a specified length, and add "..." to the end
# Given a string and a number n, truncate the string to a shorter string containing atmost n chars, For
# example, truncate("long string", 5) should return a 5 character truncated version of "long string"
# If the string gets truncated return string should have a "..." at the end. Becoz of this the smallest
# number passed in as a second argument should be 3

def truncate(str, length):
	if length < 3:
		return "Truncation must be atleast 3 characters."
	if length > len(str):
		return str
	return str[:length - 3] + '...'	
print(truncate("Hello World!", 6))					# Hel...
print(truncate("Woah", 4))							# W...
print(truncate("Woah", 3))							# ...
print(truncate("Solving problem is the best!", 10))	# Solving...
print(truncate("Super cool!", 2))					# Truncation must be atleast 3 characters.
print(truncate("Yo!", 100))							# Yo!
print("CHALLENGE 06 ends here*****************")

