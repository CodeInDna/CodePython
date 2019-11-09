#------------------OOP - Polymorphism-----------------#
# Idea of polymorphism - an object can take on many(poly) forms(morph)
# Two Different applications
# 1 The same class method works in a similar way for different classes
# 2 The same operation works for different kinds of objects

# Ist scenario The same class method works in a similar way for different classes
# A common implementation of this is to have a method in a base class that is overridden 
# by a subclass. This is known as method overriding
# Each subclass will have different implementation of the method
class Animal:
	def speak(self):
		raise NotImplementedError("Subclass needs to implement this method!")

class Dog(Animal):
	def speak(self):
		return 'Woof'

class Cat(Animal):
	def speak(self):
		return 'Meow'

class Fish(Animal):
	pass

c= Cat()
print(c.speak())	#Meow

f = Fish()
print(f.speak())	#NotImplementedError: Subclass needs to implement this method!



