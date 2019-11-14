#---------------Testing with Python-----------------#

# setUp and tearDown
# For larger applications, you might want similar application state before 
# running tests
# setUp runs before each test method
# tearDown runs after each test method
# Common Use cases: adding/removing data from a test database, creating instances of 
# a class
import unittest
from robots import Robot

class RobotTests(unittest.TestCase):
	def setUp(self):
		self.mega_man = Robot("Mega Man", battery=50)

	def test_charge(self):
		# make new robot each time 
		# mega_man = Robot("Mega Man", battery=50)	# Use setUp to make robot once 
		self.mega_man.charge()
		self.assertEqual(self.mega_man.battery, 100)

	def test_say_name(self):
		# make new robot each time 
		# mega_man = Robot("Mega Man", battery=50)	# Use setUp to make robot once 
		self.assertEqual(self.mega_man.say_name(), "BEEP BOOP BEEP BOOP. I AM MEGA MAN")
		self.assertEqual(self.mega_man.battery, 49)


if __name__=='__main__':
	unittest.main()