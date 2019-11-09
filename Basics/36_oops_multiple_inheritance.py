#------------------OOP - Multiple Inheritance-----------------#
class Aquatic:
	def __init__(self, name):
		print("AQUATIC INIT")
		self.name = name

	def swim(self):
		return f"{self.name} is swimming."

	def greet(self):
		return f"I am {self.name} of the sea."

class Ambulatory:
	def __init__(self, name):
		print("AMBULATORY INIT")
		self.name = name

	def walk(self):
		return f"{self.name} is walking."

	def greet(self):
		return f"I am {self.name} of the land."

class Penguin(Ambulatory, Aquatic):
	def __init__(self, name):
		print("PENGUIN INIT")
		# super().__init__(name)
		Ambulatory.__init__(self, name)
		Aquatic.__init__(self, name)

# jaws = Aquatic("Jaws")
# lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())		#Captain Cook is swimming.
print(captain_cook.walk())		#Captain Cook is walking.
print(captain_cook.greet())		#I am Captain Cook of the land.******WHAT?******WHY?*******
# Penguin inherits from both Aquatic and Ambulatory, therefore instances of Penguins can both 
# the walk and swim methods
# But both super classes have greet method, so which greet method will get inherited?
# The one which is called first is inherited in this scenario
# class Penguin(Ambulatory, Aquatic), then Ambulatory's greet method is inherited
# if we change the order class Penguin(Aquatic, Ambulatory), then Aquatic's greet method is inherited
# Solution: We can call the __init__ method of both parent classes nut it has one
# limitation: name property is defined twice

# But the question is still the same, why this happens?
# The answer is MRO(Method Resolution Order)
# Whenever you create a class, Python sets a Method Resolution Order(like heirarchy), for that class, which
# is the order in which Python will look for methods on instances of that class.
# We can take a refrence the MRO in three ways:
# * __mro__ attribute on the class
# * use the mro() method on the class
# * use the builtin help(cls) method

class A:
	def do_something(self):
		print("Method Defined In: A")

class B(A):
	def do_something(self):
		print("Method Defined In: B")
		super().do_something()

class C(A):
	def do_something(self):
		print("Method Defined In: C")

class D(B,C):
	def do_something(self):
		print("Method Defined In: D")
		super().do_something()
	pass

# print(D.__mro__)	#(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# print(D.mro())		#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# print(help(D))		#D B C A

thing = D()
thing.do_something()


#		A
#	  /  \
#	 B   C
#	 \  /
#	  D
# D, B, C, A, Object


# Exercise
class Mother:
	def __init__(self, eye_color, hair_color, hair_type):
		self.eye_color = eye_color
		self.hair_color = hair_color
		self.hair_type = hair_type

class Father:
	def __init__(self, eye_color, hair_color, hair_type):
		self.eye_color = eye_color
		self.hair_color = hair_color
		self.hair_type = hair_type

class Child(Mother, Father):
	pass

print(Child.mro())