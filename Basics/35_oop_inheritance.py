#------------------OOP - Inheritance-----------------#
# A class which inherits attributes and methods from another class
# In Python, inheritance works by passing the parent class as an
# argument to the definition of a child class.
class fruit:
	yummy = True

	def sanitizer_action(self):
		return "This fruit is now germs free."

class apple(fruit):
	pass

# Instance of parent class
pear = fruit()								
print(pear.yummy)						#True
print(pear.sanitizer_action())			#This fruit is now germs free.

print('*************************************')

# Instance of child class
shimla_apple = apple()
print(shimla_apple.yummy)				#True
print(shimla_apple.sanitizer_action())	#This fruit is now germs free.

print('*************************************')

print(isinstance(pear, fruit))			#True
print(isinstance(pear, apple))			#False
print(isinstance(shimla_apple, fruit))	#True
print(isinstance(shimla_apple, apple))	#True
print(isinstance(pear, object))			#True
print(isinstance(shimla_apple, object))	#True

print('*************************************')

# properties
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self._age = age
		else:
			self._age = 0

	# def age_getter(self):
	# 	return self._age

	# def age_setter(self, age):
	# 	if age >= 0:
	# 		self._age = age
	# 	else:
	# 		self._age = 0

	@property 				#kind of a getter method and we can call it without using paranthesis
	def age(self):
		return self._age

	@age.setter 			#kind of setter method and we can set the values without using paranthesis
	def age(self, new_value):
		if new_value >= 0:
			self._age = new_value
		else:
			self._age = 0

	@property
	def full_name(self):
		return f"{self.first} {self.last}" 

	@full_name.setter 
	def full_name(self, name):
		self.first, self.last = name.split(" ")

# jane = Human("Jane", "Doe", -9)		
# print(jane._age)		# 0

jane = Human("Jane", "Doe", 50)		
# print(jane.age)			#AttributeError: 'Human' object has no attribute 'age' coz of (_age)

# We can do one thing i.e. we can use getter and setter methods in order to retrieve and 
# update the values
# print(jane.age_getter())		#50
# jane.age_setter(40)
# print(jane.age_getter())		#40


# This is where properties come in
print(jane.age)				#50
jane.age = 40				#new age
print(jane.age)				#40
print(jane.full_name)			#Jane Doe
jane.full_name = "Tim Warnor"
print(jane.full_name)			#Tim Warnor
print(jane.__dict__)		#{'first': 'Tim', 'last': 'Warnor', '_age': 40}

print('*******************************')

#super(): It is used in subclass to refer the parent class
class Animal:
	isanimal = True
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		self.sound = sound
		print(f"This animal says '{self.sound *2}'")

class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		# self.name = name 				#code duplication****************AVOID
		# self.species = species		#code duplication****************AVOID

		#for avoiding code duplication we can use either of the two things

		#I
		# Animal.__init__(self, name, species)

		#II(Use super())(NOTE: No need to pass self)
		super().__init__(name, species)

		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


lulu = Cat('Lulu', 'Cat', 'Scottish Fold', 'Ball')
print(lulu)						#Lulu is a Cat
print(lulu.play())				#Lulu plays with Ball
print(lulu.make_sound('Meow'))	#This animal says 'MeowMeow'

print('*******************************')

#Another Example
class User:

	active_user = 0		# class attribute

	@classmethod
	def display_active_users(cls):			# class method*****
		return f"There are currently {cls.active_user} active users."

	@classmethod
	def from_string(cls, data_str):					#method to convert string into individual values 
		first, last, age = data_str.split(",")		#making a new instance of a class using those values
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_user += 1		# Using Class Attribute

	def __repr__(self):
		return f"{self.first} {self.last}"

	def full_name(self):
		return f"{self.first} {self.last}"
	
	def initials(self):
		return f"{self.first[0]}{self.last[0]}"

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th birthday, {self.first}"

	def logout(self):
		User.active_user -= 1
		return f"{self.first} has logged out!"

class Moderator(User):
	total_mods = 0

	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_mods += 1

	def remove_post(self):
		return f"{self.full_name} removed a post from the {self.community} community!"

	@classmethod
	def display_activemods(cls):			# class method*****
		return f"There are currently {cls.total_mods} active users."


jasmine = Moderator("Jasmine", "O'conner", 49, 'Piano')
print(jasmine)		#Jasmine O'conner
print(User.active_user)				#1
print(Moderator.active_user)		#1
user1 = User("Guddy", "Lodhi", 34)
print(User.active_user)				#2
print(Moderator.active_user)		#2
print(Moderator.total_mods)		#1
jasmine2 = Moderator("Jasmine", "O'conner", 49, 'Piano')
print(Moderator.total_mods)		#2
print(User.active_user)				#3

#This concludes there are total 3 users, out of which 2 of them are moderators
# So, we can make classmethods for the subclasses to keep track of
#instances of subclasses

