# Class Methods
# Class methods are methods(with the @classmethod decorator) that are 
# not concerned with instances, but the class itself
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

user1 = User("John","Doe",68)
user2 = User("Diana","Prince",20)
print(User.display_active_users())		#calling class method***** #There are currently 2 active users.
print(user1.display_active_users())		#calling class method***** #There are currently 2 active users.

user3 = User("John","Doe",68)
user4 = User("Diana","Prince",20)
print(User.display_active_users())		#calling class method***** #There are currently 4 active users.

user5 = User.from_string("Tom,Jones,89")
print(user5.first)	#Tom
print(user5.last)	#Jonas
print(user5.age)	#89
print(User.display_active_users())		#calling class method***** #There are currently 5 active users.

print(user5)	#Tom Jones

# __repr__method(String Representation)
# The __repr__ method is one of the several ways to provide a nicer 
# string representation
class Human:
	def __init__(self, name="somebody"):
		self.name = name

	def __repr__(self):
		return self.name

dude = Human("Jigna")
print(dude)		#Jigna

# When you try to access the instance 'print(dude)' without defining __repr__ method,
# <__main__.Human object at 0x046F7430> this would have returned

