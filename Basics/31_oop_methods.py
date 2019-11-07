#----------Object Oriented Programming(OOP) Instance Methods---------#
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

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

user1 = User("John","Doe",68)
print(user1.full_name())	#John Doe 
print(user1.initials())		#JD
print(user1.is_senior())		#True
print(user1.age)	#68
print(user1.birthday())	#Happy 68th birthday, John
print(user1.age)	#69

print("******************************")

user2 = User("Diana","Lopez",29)
print(user2.full_name())	#Diana Lopez
print(user2.initials())		#DL
print(user2.is_senior())		#False
print(user2.likes("Donuts"))	#Diana likes Donuts
print(user2.birthday())	#Happy 30th birthday, Diana

print("******************************")

#Exercise
class BankAccount:
	def __init__(self, owner):
		self.owner = owner
		self.balance = 0.0

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

acct = BankAccount("Darcy")
print(acct.owner)			#Darcy
print(acct.balance)			#0.0
print(acct.deposit(10))		#10.0
print(acct.withdraw(3))		#7.0
print(acct.balance)			#7.0

