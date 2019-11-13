#-------------------Decorators-------------------#

from random import choice
# Higher Order Functions
# We can pass funcs as args to other funcs
def add1(n, func):
	total = 0
	for i in range(n+1):
		total += func(i)
	return total

def square(x):
	return x * x

sum_of_squares = add1(10, square)
print(sum_of_squares)		#385

# We can nest functions inside one another
def greet(person):
	def get_mood():
		msg = choice(('Hello there ', 'Go away ', 'I Love you '))
		return msg

	result = get_mood() + person
	return result

print(greet("Dobby"))	#random choices (Hello there Dobby or I love you Dobby or Go away Dobby)

# We can return funcs from other funcs
# Inner functions can access outer function scope
def make_laugh_func(person):
	def get_laugh():
		l = choice(('hehehe','lol','hahaha'))
		return f"{l} {person}"

	return get_laugh

laugh = make_laugh_func("Lynda")
print(laugh())

print('*******************************')

# Decorator
# Decorators are functions
# Decorators wrap other functions and enhance their behaviour
# Decorators are examples of higher order functions
# Decorators have their own syntax, using "@" (syntactic sugar)
# In this example, we are wrapping greet fn inside be_polite function and
# enhancing its functionality
# def be_polite(fn):
# 	def wrapper():
# 		print("What a pleasure to meet you!")
# 		fn()
# 		print("Have a great day!")
# 	return wrapper

# def greet():
# 	print("My name is Dobby. ")

# def rage():
# 	print("I HATE YOU!!!")

# greet = be_polite(greet)
# greet() 
# # What a pleasure to meet you!
# # My name is Dobby.
# # Have a great day!

# polite_rage = be_polite(rage)
# polite_rage()
# # What a pleasure to meet you!
# # I HATE YOU!!!
# # Have a great day!


#Using @syntactic sugar
def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you!")
		fn()
		print("Have a great day!")
	return wrapper

@be_polite						
def greet():
	print("My name is Dobby. ")

# greet = be_polite(greet)		# **NOTE - We dont need to do this anymore, it automatically create a var(greet) and call fn
greet() 
# What a pleasure to meet you!
# My name is Dobby.
# Have a great day!

print('*******************************')

# Functions with different Signatures
def shout(fn):
	# def wrapper(name):
	def wrapper(*args, **kwargs):
		# return fn(name).upper()
		return fn(*args, **kwargs).upper()
	return wrapper

@shout
def greet(name):
	return f"Hi, I'm {name}"

@shout
def order(main, side):
	return f"Hi, I'd like the {main}, with a side of {side}, please."

print(greet("Dobby"))	# HI, I'M DOBBY
# print(order("Burger", "Fries"))	# TypeError: wrapper() takes 1 positional argument but 2 were given, when not using *args, **kwargs
print(order("Burger", "Fries"))	# HI, I'D LIKE THE BURGER, WITH A SIDE OF FRIES, PLEASE.

# We can pass *args, **kwargs to the wrapper function

print('*******************************')

from functools import wraps
# Preserving Metadata
def log_function_data(fn):
	@wraps(fn)				# ** MODIFIED CODE
	def wrapper(*args, **kwargs):
		"""I AM WRAPPER FUNCTION"""
		print(f"you are about to call {fn.__name__}")
		print(f"Here's the documentation: {fn.__doc__}")
		return fn(*args, **kwargs)
	return wrapper

@log_function_data
def add(x, y):
	"""Adds two numbers together"""
	return x + y

print(add(5, 6))
# you are about to call add
# Here's the documentation: Adds two numbers together
# 11

# (When no modules are used) Now, if we try to get the help or documentation directly from add method, it brokes up
# print(add.__doc__)
# print(add.__name__)
# print(help(add))
# I AM WRAPPER FUNCTION
# wrapper
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)
#     I AM WRAPPER FUNCTION

# for getting rid of this situation, we need to use a module called functools
# ** wraps preserves the fn's metadata, when it is decorated

print(add.__doc__)
print(add.__name__)
print(help(add))
# Adds two numbers together
# add
# Help on function add in module __main__:
# add(x, y)
#     Adds two numbers together

print('*******************************')
# Decorator Examples
from time import time

def speed_test(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start_time = time()
		result = func(*args, **kwargs)
		end_time = time()
		print(f"Executing {func.__name__}")
		print(f"Time Elapsed: {end_time - start_time}")
		return result
	return wrapper

@speed_test
def sum_nums_gen():
	return sum(x for x in range(90000000))

@speed_test
def sum_nums_list():
	return sum([x for x in range(90000000)])

# print(sum_nums_gen())	#Time Elapsed: 15.305045127868652
# print(sum_nums_list())	#Memory Error

# Another Example
def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs:
			raise ValueError("No kwargs allowed!")
		return fn(*args, **kwargs)
	return wrapper

@ensure_no_kwargs
def greet(name):
	print(f"hi there {name}")

print(greet("Michelin"))		# hi there Michelin 
# print(greet(name = "Michelin"))	# ValueError: No kwargs allowed!

print('*******************************')
# Decrator with Arguments
def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val:
				return f"First args needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner



@ensure_first_arg_is("burrito")
def fav_foods(*foods):
	print(foods)

print(fav_foods("burrito", "ice cream"))	#("burrito", "ice cream")
# fav_foods = ensure_first_arg_is("burrito")(fav_foods)
print(fav_foods("ice cream", "burrito"))	#First args needs to be burrito

print('*******************************')
def enforce(*types):
	def decorator(fn):
		def new_func(*args, **kwargs):
			new_args = []
			for (a,t) in zip(args, types):
				new_args.append(t(a))
			return fn(*new_args, **kwargs)
		return new_func
	return decorator 

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a,b):
	print(a/b)

print(repeat_msg("hello", 5))		#prints hello 5 times
print(repeat_msg("hello", '5'))		#prints hello 5 times
print(divide("1", '5'))		#0.2

