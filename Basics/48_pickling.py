#------------Pickling---------------#
# Pickle in Python is primarily used in serializing and deserializing a Python object structure. 
# it’s the process of converting a Python object into a byte stream to store it in a file/database, 
# maintain program state across sessions, or transport data over the network. 
# The pickled byte stream can be used to re-create the original object hierarchy by unpickling the stream.
import pickle
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
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat")

		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

# blue = Cat("blue", "Scottish Fold", "String")

# serialize data into another file
# with open("pets.pickle", "wb") as file:
# 	pickle.dump(blue, file)


# Unserialize data from a file
with open("pets.pickle", "rb") as file:
	zombie_blue = pickle.load(file)
	print(zombie_blue)			#blue is a Cat
	print(zombie_blue.play())	#blue plays with String
