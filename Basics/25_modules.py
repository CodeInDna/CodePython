#--------------modules--------------#
#Why use Modules?
#keep Python files small
#Reuse code across multiple files by importing
#A module is just a python file

#Built-in Modules
# import random as rand
# print(rand.choice(["apple", "banana", 'pineapple', 'cherry']))	#choose the random item from the list
# print(rand.randint(1, 100))	#gives the random number from the range


from random import choice, randint, shuffle
print(choice(["apple", "banana", 'pineapple', 'cherry']))	#choose the random item from the list
print(randint(1, 100))	#picks a random number from the given range
lst = ["apple", "banana", 'pineapple', 'cherry']
shuffle(lst)		#shuffles the list
print(lst)	

#Exercises
import math 
print(math.sqrt(1519))

#contains_keyword : accepts any no of args. It should return True if any of the args
#are considered Python keywords(like "def", "return", "if"etc). Otherwise should return 
#False. Built-in module "keyword" can be used that contains a method called "iskeyword"
from keyword import iskeyword
def contains_keyword(*args):
	return any(iskeyword(arg) for arg in args)
print(contains_keyword("hello", "goodbye"))	#False
print(contains_keyword("def", "haha", "chicken")) #True


#Different ways to import
# import random
# import random as so_random
# from random import *
# from random import choice, randint
# from random import choice as gimme_one, randint as gimme_one_int

