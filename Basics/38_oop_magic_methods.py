#------------------OOP - Magic Methods-----------------#
# In this example 8 + 2 #10
# "8" + "2" 	#82
# The '+' operator is a shorthand for a special method called __add__()
# that gets called on the first operand
# If the first(left) operand is a instance of int, __add()__ does mathematical addition.
# If it's a string, it does string concatenation
from copy import copy
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def __repr__(self):
		return f"Human named: {self.first} {self.last} aged {self.age}"

	def __len__(self):
		return self.age

	def __add__(self, other):
		if isinstance(other, Human):
			return Human(first='NewBorn', last=self.last, age=0)
		return "You can't add that"

	def __mul__(self, other):
		if isinstance(other, int):
			return [copy(self) for i in range(other)]
		return "Can't Multiply!"

k = Human("Kevin", "Jones", 47)
j = Human("Jenny", "Lopez", 34)
print(j)		# Human named: Jenny Lopez
print(len(j))	# 34
print(j + k)		# Human named: NewBorn Lopez aged 0
print(j * 2)		# [Human named: Jenny Lopez aged 34, Human named: Jenny Lopez aged 34]
print(j * 'a')		# Can't Multiply!

triplets = j * 3
triplets[1].first = 'Jessica'
# When copy module is not used, if you change the name of one of the triplets, all points to same object
# print(triplets)	#[Human named: Jessica Lopez aged 34, Human named: Jessica Lopez aged 34, Human named: Jessica Lopez aged 34]

# When you use copy module, all are treated individually
print(triplets)		#[Human named: Jenny Lopez aged 34, Human named: Jessica Lopez aged 34, Human named: Jenny Lopez aged 34]

# Kevin and Jessica having triplets
print((k + j) * 3)	# [Human named: NewBorn Jones aged 0, Human named: NewBorn Jones aged 0, Human named: NewBorn Jones aged 0]


# Special method Train
class Train:
	def __init__(self, num_cars):
		self.num_cars = num_cars

	def __repr__(self):
		return f"{self.num_cars} car train"

	def __len__(self):
		return self.num_cars

a_train = Train(4)
print(a_train)		#4 car train
print(len(a_train))	#4