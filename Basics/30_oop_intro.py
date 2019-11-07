#----------Object Oriented Programming(OOP)---------#
# What is OOP?
# OOP is a method of programming that attempts to model some 
# process or thing in the world as a 'class' or 'object'.

# What is 'class'? 
# A "blueprint" for objects. Classes can contain methods 
# (functions) and attributes(similar to keys in a dict)

# What is 'instance'?
# Objects that are constructed from a class blueprint that
# contains their class's methods and properties

# Why OOP?
# With OOP, the goal is to encapsulate your code into logical.
# heirarchical grouping using "classes" so that you can reason
# about your code at a higher level

# Encapsulation
# Using OOP in Python, we can restrict access to methods and variables.
# This prevent data from direct modification which is called encapsulation.
# In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.

# Abstraction
# Abstraction means hiding the complexity and only showing the essential 
# features of the object. So in a way, Abstraction means hiding the real 
# implementation and we, as a user, knowing only how to use it.
# Real world example would be a vehicle which we drive with out caring or knowing what all is going underneath.

# DEFINING OUR FIRST CLASS
class User:
	pass

user1 =  User()		# making an instance(instantiation)
print(type(user1))	# <class '__main__.User'>


# Another simple class
class Vehicle:
	pass

car = Vehicle()	#object1
boat = Vehicle()	#object1
print(car)
print(boat)


# Moving to __init__ method
# Classes in Python can have a special __init__ method, which gets
# called every time you create an instance of the class
# (just like constructor in other languages)
# self refers to the current class instance. By using the "self" 
# keyword we can access the attributes and methods of the class 
# self always be the first parameter to __init__ and any methods and 
# properties on class instance
class Student:
	def __init__(self, first, last, age):
		# print("A new student took admission!")
		self.first = first
		self.last = last
		self.age = age

student1 = Student("Vidhya", "Baagji", 40)
student2 = Student("Rahul", "Saxena", 50)
print(student1.first, student1.last)	#Vidhya Baagji
print(student2.first)	#Rahul


# Exercise
class Comment:
	def __init__(self, username, text, likes=0):
		self.username = username
		self.text = text
		self.likes = likes

c = Comment("rosa77", "soooooo cute!", 3)
print(c.username)	# Vidhya Baagji
print(c.text)		# Rahul
print(c.likes)		# rosa77

another_comment = Comment("daniel", "lolllllll!")
print(another_comment.username)	# daniel
print(another_comment.text)		# lolllllll!
print(another_comment.likes)	# 0


# Underscores Dunder Methods Name Mangling and More

# 1. _var: The underscore prefix is meant as a hint to another 
# programmer that a variable or method starting with a single 
# underscore is intended for internal use.
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
t = Test()
print(t.foo)	#11
print(t._bar)	#23
# We just saw that the leading single underscore in _bar did not 
# prevent us from “reaching into” the class and accessing the value of that variable.
# That’s because the single underscore prefix in Python is merely an agreed upon 
# convention—at least when it comes to variable and method names.
# However, leading underscores do impact how names get imported from modules.
# This is my_module.py:
# def external_func():
#     return 23

# def _internal_func():
#     return 42
# Now if you use a wildcard import to import all names from the module, 
# Python will not import names with a leading underscore (unless the module 
# defines an __all__ list that overrides this behavior)
#  from my_module import *
#  external_func()
# 23
#  _internal_func()
# NameError: "name '_internal_func' is not defined"

# 2. var_ : A single trailing underscore (postfix) is used by convention to 
# avoid naming conflicts with Python keywords.
# def make_object(name, class):	#SyntaxError: "invalid syntax"

def make_object(name, class_):
	pass 

# 3. __var: This is also called name mangling—the interpreter changes the name 
# of the variable in a way that makes it harder to create collisions when the class 
# is extended later.
class Person:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23	#name mangling
t = Test()
print(dir(t)) # ['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__'.....]
# If you look closely you’ll see there’s an attribute called _Test__baz on this object. 
# This is the name mangling that the Python interpreter applies. 
# It does this to protect the variable from getting overridden in subclasses.
# Let’s create another class that extends the Test class and attempts 
# to override its existing attributes added in the constructor:
class ExtendedPerson(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'
t2 = ExtendedPerson()
print(t2.foo) 		#'overridden'
print(t2._bar)     #'overridden'
print(t2.__baz)    #AttributeError: "'ExtendedTest' object has no attribute '__baz'"

# __var__: leading and trailing double underscores are reserved for special use in the language. 
# This rule covers things like __init__ for object constructors, or __call__ to make an object callable.
# It’s best to stay away from using names that start and end with double underscores (“dunders”) in your
# own programs to avoid collisions with future changes to the Python language.