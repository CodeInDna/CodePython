#---------------Testing with Python-----------------#
# Test Driven Development
# * Development begins by writing tests
# * Once tests are written, write code to make tests pass
# * Once tests pass, a feature is considered complete

# Red, Green, Refactor
# * Red - Write a test that fails
# * Green - Write the minimal amount of code necessary to make the test pass
# * Refactor - Clean up the code, while ensuring that tests still pass

# Assertions
# * We can make simple assertions with the assert keyword
# * assert accepts an expression
# * Returns None if the exp is truthy
# * Raises an AssertionError if the exp is falsy
# * Accepts an optional error message as a second argument
# Assertions Warning
# If Python file is running with the -O(Optimised) flag,
# assertions will not be evaluated

def add_postitve_numbers(x, y):
	assert x > 0 and y > 0, "Both numbers must be positive!"
	return x + y

print(add_postitve_numbers(1, 1))		#2
# print(add_postitve_numbers(1, -1))		#AssertionError: Both numbers must be positive!

def eat_junk(food):
	assert food in [
	"pizza",
	"burger",
	"ice cream",
	"fried butter"
	], "Food must be a junk food!"
	return f"NOM NOM NOM I am eating {food}"
food = input("Enter a food please : ")
print(eat_junk(food))
# input='oats'
# output=AssertionError: Food must be a junk food!

# Doctests
# We can write tests for functions inside of the docstring
# Write code that looks like it's inside of REPL
# To run in powershell :  python -m doctest -v .\41_testing_with_python.py

def add(a, b):
	"""
	>>> add(2, 3)
	5

	>>> add(100, 200)
	300
	"""
	return a + b    #Test passed.
	# return a * b 	# ***Test Failed*** 2 failures.

def double(values):
	"""doubles the values in a list

	>>> double([1,2,3,4])
	[2, 4, 6, 8]

	>>> double([])
	[]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']

	>>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
	"""
	return [2 * el for el in values]	# Test passed.

# Issues when it result in failture although it looks perfectly fine
def say_hi():
	"""
	>>> say_hi()
	"hi"		
	"""
	return "hi"	#***Test Failed*** 1 failures.
# Expected:
#     "hi"
# Got:
#     'hi'	


def true_that():
	"""

	>>> true_that()
	True 
	"""
	return True	# ***Test Failed*** 1 failures.
# Expected:
#     True
# Got:
#     True
# NOTE: No idea why test got failed??? Well it counts spacing too, I left a space after 
# 'TRUE ' :( ....How DISAPPOINTING ARRRGGGGHHHH...


def make_dict(keys):
	"""
	>>> make_dict(['a','b'])
	{'b': True, 'a': True}
	"""
	return {key: True for key in keys}	#***Test Failed*** 1 failures.
# Expected:
#     {'b': True, 'a': True}
# Got:
#     {'a': True, 'b': True}
# That is too MUCCCHHHHH


#Issues with doctests
# * Syntax is a little strange
# * Clutters up our function code
# * Lacks many features of larger testing tools
# * Tests can be brittle
