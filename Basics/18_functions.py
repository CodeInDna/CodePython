#------------functions--------------#
def greet():	#function defination
	print("Namastey!")

greet()	#call function

#return values from a function
def print_square_of_3():
	return 3**2
result = print_square_of_3()
print(result )


#returning list of even numbers
def even_nos():
	return [num for num in range(1,50) if num % 2 ==0]
evens = even_nos()
print(evens)

#parameters
def square(x):
	return x ** 2
sq = square(5)
print(sq)


def add(a,b):
	return a+b
add = add(2,5)
print(add)

def yell(str):
	return str.upper() + '!'
print(yell("shut up"))
print(yell("keep ur mouth shut"))


#default parameter
def exponent(num, power = 4):
	return num ** power
print(exponent(3))
print(exponent(5))

#passing function as parameter
def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def math(a,b, fn=add):
	return fn(a,b)

print(math(2,5))
print(math(2,5, subtract))

def speak(animal='dog'):
	if animal == 'pig':
		return 'oink'
	elif animal == 'duck':
		return 'quack'
	elif animal == 'cat':
		return 'meow'
	elif animal == 'dog':
		return 'woof'
	return "?"

print(speak())
print(speak('pig'))
print(speak('duck'))
print(speak('cat'))
print(speak('dog'))
print(speak('apple'))

#or

# def speak(animal="dog"):
#     noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"

#keyword arguments(When calling the fn we can specify which argument corresponds to which parameter)
def full_name(first, last):
	return "Your name is "+ first + " " +last

print(full_name(first = "Nisha", last = "Gupta"))
print(full_name(last = "Trivedi", first = "Bala"))

#Scope
#variable defined outside the function can be retrieved inside fn
teacher = "Manisha"
def greetings():
	return "hello " + teacher
print(greetings())

#variable defined inside the fn cannot be retrieved outside it
def greeting():
	name = "meme"
	return "hello " + teacher
print(full_name)		#NameError: name 'name' is not defined

#global (if we try to manipulate the global variable(without telling explicitly that i m using global variable) inside a fn it will throw an error)
total = 0
# def increment():
# 	return total += 1

def increment():
	global total
	total += 1
	return total

print(increment())

#nonlocal(let us modify a parent's variable in child(aka child) function)
def outer():
	count = 0
	def inner():
		nonlocal count
		count += 1
		return count
	return inner()
print(outer())


#documenting function
def expo(num, power):
	"""expo(num, power) raises num to specified power. Power defaults to 2."""
	return num ** power
print(expo(2,3))
print(expo.__doc__)