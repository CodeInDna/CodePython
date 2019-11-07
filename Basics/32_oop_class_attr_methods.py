#-----------OOP Class Attributes & Methods------------#
# We can define attributes directly on a class that are 
# shared by all instances of a class and the class itself.
class User:

	active_user = 0		# class attribute

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_user += 1		# Using Class Attribute

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

print(User.active_user)		#0	Calling class attribute
user1 = User("John","Doe",68)
user2 = User("Diana","Prince",20)
print(User.active_user)		#2
user1.logout()
print(User.active_user)		#1