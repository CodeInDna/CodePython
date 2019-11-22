print("CHALLENGE 01 starts here*****************")
# Create a function letter_counter which accepts a string and return a function.
# When the inner fn is invoked it should accept a parameter which is a letter,
# and the inner fn should return the number of times that the letter appears. This inner
# fn should be case sensitive

def letter_counter(str):
	def count_letter(letter):
		return str.lower().count(letter.lower())
	return count_letter
counter = letter_counter('Amazing')
print(counter('a'))	# 2
print(counter('m'))	# 1
print(counter('M'))	# 1
print("CHALLENGE 01 ends here*****************")



print("CHALLENGE 02 starts here*****************")
# Create a function once which accepts a fn and returns a new fn that can only be invoked once.
# if it is invoked more than once then it should return none. Hint: you will need to define a new fn 
# inside of your once fn and return that fn. You can add prop to your inner fn to see if it has run already
def add(a,b):
	return a+b

def once(fn):
	already_run = True
	def inner(*args):
		nonlocal already_run 
		if already_run:
			already_run = False
			return fn(*args)
		return None
	return inner
	
oneaddition = once(add)		# [1, 10]
print(oneaddition(2,2))	# 4
print(oneaddition(2,2))	# None
print(oneaddition(2,2))	# None
print("CHALLENGE 02 ends here*****************")


print("CHALLENGE 03 starts here*****************")
# Create a function next_prime which returns a generator that will yield an unlimited number
# of primes, starting from the first prime(2)
from math import sqrt
def is_prime(num):
	if num <= 1:
		return False
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	i = 3
	while i <= sqrt(num):
		if num % i == 0:
			return False
		i += 2
	return True

def next_prime():
	num = 1
	while True:
		prime = is_prime(num)
		if prime:
			yield num
		num += 1

prime_gen = next_prime()
print(next(prime_gen))	# 2
print(next(prime_gen))	# 3
print(next(prime_gen))	# 5
print(next(prime_gen))	# 7
print(next(prime_gen))	# 11
print(next(prime_gen))	# 13
print(next(prime_gen))	# 17
print(next(prime_gen))	# 19
print(next(prime_gen))	# 23
print("CHALLENGE 03 ends here*****************")