#--------------debugging part 2--------------#

#Raise your own EXCEPTION
#We can also throw errors using the "raise" keyword

# raise ValueError('Invalid VALUE')	#ValueError: Invalid VALUE
# raise NameError('Name not found!')	#NameError: Name not found!

def colorize(text, color):
	colors = ['cyan', 'orange', 'black', 'lightblue', 'pink']
	if type(text) is not str:
		raise TypeError('Text must be a string')
	if type(color) is not str:
		raise TypeError('Color must be a string')
	if color not in colors:
		raise ValueError('Invalid Color')
	print(f"Printed {text} in {color} color")
colorize("hello", "cyan")	#Printed hello in cyan color
# colorize([], "cyan")		#TypeError: Text must be a string***************ERROR
# colorize("hello", 12)		#TypeError: Color must be a string***************ERROR
# colorize("hello", "red")	#ValueError: Invalid Color***************ERROR


#Handle Errors
#In Python, it is strongly encouraged to use try/except blocks,
#to catch exceptions when we can do something about them

# try:
# 	foobar
# except:
# 	print("PROBLEM")		#PROBLEM
# print("Hell Yeah")		#Hell Yeah

def get(d, key):
	try:
		return d[key]
	except KeyError:
		return None
d = {"name":"Ricky"}
print(get(d, 'name'))		#Ricky
print(get(d, 'city'))		#None

# try:
# 	num = int(input("Please enter a number: "))
# except:
# 	print("That's not a number!")	#except will run when try is falsy
# else:
# 	print(f"You've entered {num}")	#else will run when except does not
# finally:
# 	print("RUNS NO MATTER WHAT!")	

#keep asking until user hit a number
while True:
	try:
		num = int(input("Please enter a number: "))
	except ValueError:
		print("That's not a number!")	#except will run when try is falsy
	else:
		print(f"You've entered {num}")	#else will run when except does not
		break
	finally:
		print("RUNS NO MATTER WHAT!")	


def divide(a,b):
	try:
		result =  a/b
	except ZeroDivisionError:
		print("dont divide by zero please!")
	except TypeError as err:
		print("a and b must be int or float")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")
print(divide(1,2))			#1 divided by 2 is 0.5
print(divide(1,'a'))#a and b must be int or float, unsupported operand type(s) for /: 'int' and 'str', None

#Debugging with pdb(python debugger)
