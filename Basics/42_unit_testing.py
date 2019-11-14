#---------------Testing with Python-----------------#

# Unit Testing
# Test smallest parts of an application in isolation(e.g. units)
# Good candidates for unit testing: individual classes, modules or fns
# Bad candidates for unit testing: an entire application, dependencies
# across several classes or modules
# Python comes witha built-in module called unittest
# You can write unit tests encapsulated as classes that inherits from unittest.TestCase
# This inheritance gives you access to many assertion helpers that lets you test the behaviour 
# of your functionsYou can run tests by calling unittest.main()
# Run this file using command: python .\42_unit_testing.py -v : It will show everything in detail
import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
	def test_eat_healthy(self):
		self.assertEqual(
			eat("broccoli", ishealthy=True),
			"I'm eating broccoli, because my body is a Temple."
			)

	def test_eat_unhealthy(self):
		self.assertEqual(
			eat("pizza", ishealthy=False),
			"I'm eating broccoli, because YOLO."
			)

	def test_eat_healthy_boolean(self):
		with self.assertRaises(ValueError):
			eat('pizza', ishealthy="who cares?")

	def test_short_nap(self):
			self.assertEqual(
				nap(1),
				"I'm feeling refreshed after my 1 hour nap"
				)

	def test_long_nap(self):
			self.assertEqual(
				nap(3),
				"Ugh I overslept. I didn't mean to nap for such long hours!"
				)

	def test_is_funny(self):
		# self.assertEqual(is_funny("tim"), False)
		self.assertFalse(is_funny("tim"), "Tim should not be funny")

	def test_is_funny_anyone_else(self):
		self.assertTrue(is_funny("blue"), "blue should be funny")
		self.assertTrue(is_funny("tammy"), "tammy should be funny")
		self.assertTrue(is_funny("sven"), "sven should be funny")

	def test_laugh(self):
		self.assertIn(laugh(), ('lol','haha','hehe'))


if __name__ == "__main__":
	unittest.main()