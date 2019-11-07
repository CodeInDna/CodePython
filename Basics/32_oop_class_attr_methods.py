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


#More about Class Attributes
class Pet:
	allowed = ["cat", "dog", "fish", "rat"]
	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self, species):		#update species attribute
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Princy", "cat")
dog = Pet("Browny", "dog")
# tiger = Pet("jfjfh", "tiger")	#ValueError: You can't have a tiger pet!

print("******************************")

# We can update the species directly using below code, but
# we need to get a better option to update the attributes 
# so, we gonna use 'set_species' method defined above
print(dog.species)		#dog
dog.species = "gibrish"
print(dog.species)		#gibrish

#Now, we can update the species using a method
dog.set_species("dog")
print(dog.species)		#dog
# dog.set_species("tiger")	#ValueError: You can't have a tiger pet!


#Also, We can add more species in allowed variable
Pet.allowed.append("pig")
print(Pet.allowed)	#['cat', 'dog', 'fish', 'rat', 'pig'] 


#So, defining attributes directly on a class is shared by all instances
#of a class(cat, dog and Pet shares same id for the allowed attribute)
#check it out:
print(id(Pet.allowed))	# 62846344
print(id(cat.allowed))	# 62846344
print(id(dog.allowed))	# 62846344

#if we change cat.allowed, it doesn't make any change dog.allowed or Pet.allowed
#They won't be same thing anymore
cat.allowed = ['tiger','bear']
print(cat.allowed)	#['tiger','bear']	
print(Pet.allowed)	#["cat", "dog", "fish", "rat", "pig"]
print(dog.allowed)	#["cat", "dog", "fish", "rat", "pig"]


#Exercise
class Chicken:

	total_eggs = 0	# Class Attribute

	def __init__(self, name, species):
		self.name = name
		self.species = species
		self.eggs = 0

	def lay_eggs(self):			# Instance Method
		self.eggs += 1
		Chicken.total_eggs += 1
		return self.eggs

c1 = Chicken(name = "Alice", species = "Partridge Silkie")
c2 = Chicken(name = "Amelia", species = "Speckled Sussex")
print(Chicken.total_eggs)	#0
c1.lay_eggs()
print(Chicken.total_eggs)	#1
c2.lay_eggs()
c2.lay_eggs()
print(Chicken.total_eggs)	#3
