#--------------Json (JavaScript Object Notation)---------#
import jsonpickle
class Cat:
	def __init__(self, name, breed, toy):

		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

c = Cat("Kitty", "Tabby", "Ball")

with open("cat.json", "w") as file:
	frozen = jsonpickle.encode(c)
	file.write(frozen)

# with open("cat.json", "r") as file:
# 	contents = file.read()
# 	unfrozen = jsonpickle.decode(contents)
# 	print(unfrozen)