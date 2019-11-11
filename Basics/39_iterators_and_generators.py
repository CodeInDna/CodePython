#--------------Iterators and Generators--------------#
# Iterable - An object which will return an iterator when iter()
# is called on it
# Iterator - An object that can be iterated upon. An object which returns
# data, one element at a time when next() is called on it. 

#"HELLO" is an iterable, but it is not an iterator
# iter("HELLO") returns an iterator
name = "Vishakha"
# print(next(name))		# TypeError: 'str' object is not an iterator

it = iter(name)
print(it)			# <str_iterator object at 0x03F57148>
print(next(it))		# V
print(next(it))		# i
print(next(it))		# s
print(next(it))		# h
print(next(it))		# a
print(next(it))		# k
print(next(it))		# h
print(next(it))		# a
# print(next(it))		# StopIteration

# for loop first call iter method on iterable and convert it into iterator
# and then call next method on that iterator which returns next item until
# it raises a StopIteration error

print('*******************************')

# Custom For loop
def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			i = next(iterator)
		except StopIteration:
			print("END OF ITERATOR")
			break
		else:
			func(i)
def square(x):
	print(x * x)

my_for("hello", print)
my_for([1,2,3,4,5], square)

print('*******************************')

# Custom Iterator
class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration

for x in Counter(0,10):
	print(x)

print('*******************************')

# Making Deck class Iterable
from random import shuffle

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:
	def __init__(self):
		suits = ["Hearts","Spades","Diamonds","Clubs"]
		values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
		self.cards = [Card(suit, val) for suit in suits for val in values]

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def __iter__(self):
		return iter(self.cards)

	def count(self):
		return len(self.cards)

	def _deal(self, number):
		cards_in_deck = self.count()
		to_remove = min(cards_in_deck, number)
		if cards_in_deck == 0:
			raise ValueError("All cards have been dealt!")
		cards_removed = self.cards[-to_remove:]
		self.cards = self.cards[:-to_remove]
		return cards_removed

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled!")
		shuffle(self.cards)
		return self

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

my_deck = Deck()
my_deck.shuffle()

for card in my_deck:
	print(card)
print('*******************************')

# Generators
# Generators are iterators
# It is a short way of creating iterators
# Generators can be created with genetator functions
# It uses the yield keyword
# It can be created with generator expressions
# Generators consumes lesser memory than list or any other data structure

# In the below example, while first check whether the number is less than max or not,
# if it is, then yield count(which halts the further process until next() is called upon it)
# It always stores one thing at a time
def count_up_to(max):
	count = 1
	while count <= max:
		yield count
		count += 1
print(count_up_to(5)) #<generator object count_up_to at 0x03FD1B50>
gen = count_up_to(5)
print(next(gen))		#1
print(next(gen))		#2
print(next(gen))		#3
print(next(gen))		#4
print(next(gen))		#5
# print(next(gen))		#StopIteration


#Exercise
def week():
	days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	for day in days_of_week:
		yield day
days = week()
print(next(days))	# Monday
print(next(days))	# Tuesday
print(next(days))	# Wednesday
print(next(days))	# Thursday
print(next(days))	# Friday
print(next(days))	# Saturday
print(next(days))	# Sunday


def yes_or_no():
	status = 'yes'
	while True:
		yield status
		status = 'no' if status == 'yes' else 'yes'
switch = yes_or_no()
print(next(switch))	# yes		
print(next(switch))	# no
print(next(switch))	# yes
print(next(switch))	# no

print('*******************************')

# Infinite Generator

#Using regular function (Repeating things after end of list or tuples)
# def current_beat():
# 	max = 100
# 	nums = (1,2,3,4)
# 	i = 0
# 	result = []
# 	while len(result) < max:
# 		if i >= len(nums): i = 0
# 		result.append(nums[i])
# 		i += 1
# 	return result
# print(current_beat())

# Using Generators
def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums) : i = 0
		yield nums[i]
		i += 1
beat = current_beat()
print(next(beat))	# 1
print(next(beat))	# 2
print(next(beat))	# 3
print(next(beat))	# 4
print(next(beat))	# 1

print('***************************************************')

def make_song(count=99, beverage='soda'):
	while count >= 0:
		if count > 1: msg = f"{count} bottles of {beverage} on the wall."
		elif count == 1: msg = f"Only {count} of {beverage} on the wall."
		else: msg = f"No more {beverage}."
		count -= 1
		yield msg
song = make_song(5, 'Pineapple Juice')
print(next(song))	#5 bottles of Pineapple Juice on the wall.
print(next(song))	#4 bottles of Pineapple Juice on the wall.
print(next(song))	#3 bottles of Pineapple Juice on the wall.
print(next(song))	#2 bottles of Pineapple Juice on the wall.
print(next(song))	#Only 1 of Pineapple Juice on the wall.
print(next(song))	#No more Pineapple Juice.
# print(next(song))	#StopIteration

print('***************************************************')

#Fabonacci Series 
# Using list
def fab_list(max):
	a, b = 0, 1
	nums = []
	while len(nums) < max:
		nums.append(b)
		a, b = b, a+b
	return nums
print(fab_list(10))	# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Using generator
def fib_gen(max):
	x = 0
	y = 1
	count = 0
	while count < max:
		x, y = y, x + y
		yield x
		count += 1
fib = fib_gen(10)
print(next(fib))	# 1
print(next(fib))	# 1
print(next(fib))	# 2
print(next(fib))	# 3
print(next(fib))	# 5
print(next(fib))	# 8
print(next(fib))	# 13
print(next(fib))	# 21
print(next(fib))	# 34
print(next(fib))	# 55
# print(next(fib))	# StopIteration

print('***************************************************')

def get_multiples(number = 1, count = 10):
	counter = 1
	while counter <= count:
		yield number * counter
		counter += 1

#OR

# def get_multiples(num=1, count=10):
#     next_num = num
#     while count > 0:
#         yield next_num
#         count -= 1
#         next_num += num

multiples = get_multiples(5, 5)
print(next(multiples))		# 5
print(next(multiples))		# 10
print(next(multiples))		# 15
print(next(multiples))		# 20
print(next(multiples))		# 25
# print(next(multiples))		# StopIteration

print('***************************************************')

def get_unlimited_multiples(number = 1):
	counter = 1
	while True:
		yield number * counter
		counter += 1
un_mult = get_unlimited_multiples(5)
print(next(un_mult))		# 5
print(next(un_mult))		# 10
print(next(un_mult))		# 15
print(next(un_mult))		# 20
print(next(un_mult))		# 25
print(next(un_mult))		# 30
# .....and it keeps going


#Generator Expressions (We use paranthesis for generator exp)
import time
gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_total_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_total_time = time.time() - list_start_time

print(gen_total_time)	# 1.545854091644287
print(list_total_time)	# 1.674522876739502



