#We use lambda functions when we require a 
#nameless function for a short period of time.
#Python, we generally use it as an argument to a 
#higher-order function (a function that takes in 
#other functions as arguments). 
def square(num): return num * num		#named function

square2 = lambda num: num * num		#lambda(anonymous) function

print(square(4))
print(square2(3))
print(square.__name__)		#square
print(square2.__name__)		#lambda

#cube
cube = lambda num: num**3
print(cube(8))


#map fn : accepts two args, a function and 
#an iterable(something that can be iterated over like lists, strings, dictionaries etc)
#runs the lambda for each value in the iterable and return a map object which can be
#converted into another data structure
nums = [1,2,3,4,5]
doubles = map(lambda x: x*2, nums)	#<map object at 0x043B7178>
doubles = list(doubles)		#convert map object into list
print(doubles)

#Map Time Exercise 
#decrement_list : accpets a single list of nos as a parameter, it should return a copy
#of the list where each item has been decremented by one.
def decrement_list(num_list): return list(map(lambda x:x-1, num_list))
print(decrement_list([1,2,3]))	#[0,1,2]


#filter fn : filter returns only the object which are True to the condition passed in
li = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, li))	
print(evens)	#[2,4]

#combining filter and map
#return a new list with the string "Your instructor is "+ each value in the array, 
#but only if the value is less than 5 characters
names = ['Lassie', 'Rusty', 'Mona','Tina']
list_of_instructors = list(map(lambda name:f"Your instructor is {name}", filter(lambda x:len(x) < 5, names)))
print(list_of_instructors)	#['Your instructor is Mona']

#above example using list comprehension
print([f"Your instructor is {name}" for name in names if len(name) < 5])


#Filter Exercise 
#remove_negatives fn : accepts a list of nos and returns a copy of lists with
#all negative nos removed
def remove_negatives(li): return list(filter(lambda x:x>=0, li))
print(remove_negatives([1,2,0,-1,-4]))


#all : returns True if all elements of the iterable are truthy(or if the iterable is empty)
vowels = all([char for char in 'eio' if char in 'aeiou'])	
print(vowels)		#True

people = ["Charlie", "Clarie", "Commi", "Belkin"]
starts_with_C = all([person[0] == 'C' for person in people])
print(starts_with_C)

#any : returns True if any element of the iterable is truthy. 
#If the iterable is empty, returns False
nums = [1,2,3,4,5]
any_odds = any([num % 2 != 0 for num in nums])
print(any_odds)			#True

#Generator Expressions : We dont have to add list comprehension brackets unless we need it
#in the above example we can do this as well
any_odds2 = any(num % 2 != 0 for num in nums)
print(any_odds2)		#True

# Using sys.getsizeof
#list comprehension takes more memory than generator expression
import sys
list_comprehension = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("It take... ")
print(f"List Comprehension: {list_comprehension} bytes ")
print(f"Generator Expression: {gen_exp} bytes ")

#Any/All Exercise
#is_all_strings fn : accepts a single iterable and returns True 
#if it contains ONLY strings, otherwise return False
def is_all_strings(iterable): return all(type(val)==str for val in iterable)
print(is_all_strings(['a','b','c']))
print(is_all_strings(['a','b','c', 5]))


#sorted method : return a new sorted list from the items in iterable
#it works on anything that is iterable
#it does not change the original iterable

#ascending order
more_nums = [6,1,3,4]
sorted_list = sorted(more_nums)	
print(sorted_list)	#[1,3,4,6]
print(more_nums)	#[6,1,3,4]

#descending order(reverse sorting)
more_nums1 = [6,1,3,4]
sorted_list1 = sorted(more_nums1, reverse=True)	
print(sorted_list1)	#[6,4,3,1]

sort_tuple = sorted((2,1,45,6,3,32))
print(sort_tuple)

songs = [
		{"title": "happy birthday!", "playcount": 1},
		{"title": "toxic!", "playcount": 12},
		{"title": "senorita", "playcount": 67},
		{"title": "waka waka", "playcount": 36}	
]
sorted_playcount = sorted(songs, key=lambda s:s['playcount'])
sorted_playcount_rev = sorted(songs, key=lambda s:s['playcount'], reverse=True)
print(sorted_playcount)
print(sorted_playcount_rev)

#max and min method (return the largest and smallest item from the iterable)
print(max(1,2,4,5,7,32))	#32
print(max('awesome'))		#w
print(max('a','b','d'))		#d
print(min(1,2,4,5,7,32))	#1

names = ['Arya', 'Arunima', 'Tim']
print(min(len(name) for name in names))	#3

largest_name = max(names, key=lambda n:len(n))
print(largest_name)

#get least no of playcount
least_plays = min(songs, key = lambda s:s['playcount'])
least_plays_title = min(songs, key = lambda s:s['playcount'])['title']
print(least_plays)
print(least_plays_title)

#max and min exercise
#extreme fn : accpets an iterable, return a tuple containing the min & mac elements
def extreme(iterable): return (min(iterable), max(iterable))
print(extreme([1,2,3,4,5]))
print(extreme((99,25,30,-7)))
print(extreme("alcatraxz"))

#reversed : return a reverse iterator
nos = [1,2,3,4]
# reverse fn
nos.reverse()	#reverses the original list
print(nos) 	#[4, 3, 2, 1]

nos1 = [1,2,3,4,5]
#reversed fn
res = reversed(nos1)
print(res)	#<list_reverseiterator object at 0x038E74D8> - so that we can iterate over it in reverse order
for num in reversed(nos1):
	print(num-1)


#len built-in fn
print(len('hello'))		#5
#OR
print('hello'.__len__())		#5

#abs() sum() round()
#abs() : returns the absolute value of a no. Argument may be an integer or a floating point number
print(abs(-3))
print(abs(3))

#sum() takes an iterable and an optional start, returns the sum of start and the items of an iterable
#from left to right and returns the total
#start default from zero
#sum cannot be used for summing strings
print(sum([1,2,3], 10))		#16
print(sum([1,2,3], -6))		#0
print(sum((1.5,2,3.7)))		#7.2

#round() returns the rounded to ndigits precision after the decimal point.
#if ndigits is ommited or is None, it returns the nearest integer to its input
print(round(10.2))		#10
print(round(1.212121))		#1
print(round(3.51234))		#4
print(round(3.51234,3))		#3.512


#Greatest Magnitude Exercise
#max_magnitude fn : accepts a single list full of nos. 
#It should return the magnitude of the nos with the largest 
#magnitude(the no that is furthest away from zero)
# def max_magnitude(lst):
# 	new_lst = []
# 	for mag in lst:
# 		new_lst.append(abs(mag))
# 	return max(new_lst)

def max_magnitude(lst):
	return max(abs(mag) for mag in lst)
print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))


#sum_even_values fn : accepts a variable no of arguments and return the sum of all 
#the arguments that are divisible by 2. If there are no nos divisible by 2, the function 
#should return 0. To be clear, it accepts all the nos as individual args
def sum_even_values(*args):
	return sum(num for num in args if num % 2 == 0)
print(sum_even_values(1,2,3,4,5,6))	#12
print(sum_even_values(4,2,1,10))	#16
print(sum_even_values(1))			#0


#sum_floats fn : accepts a variable no of arguments, It should return the sum of all 
#the parameter that are floats. IF no floats fn should return 0
def sum_floats(*args):
	return sum(num for num in args if type(num) == float)
print(sum_floats(1.5, 2.4, 'awesome', [], 1))	#3.9
print(sum_floats(1,2,3,4,5))					#0

#zip: Make an iterator that aggregates elements from each of the iterables
#returns an iterator of tuples, where the i-th tuple contains i-th element
#from each of the argument sequences or iterables
#The iterator stops when the shortest input iterable is exhausted
lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]
lst3 = ["hi","lol","kkrh"]
zip1 = zip(lst1, lst2)
zip2 = zip(lst1, lst2, lst3)
print(zip1) #<zip object at 0x04006AE8>
print(list(zip1))	#[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print(list(zip2))	#[(1, 6, 'hi'), (2, 7, 'lol'), (3, 8, 'kkrh')]	#stops at shortest list


midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']
# need to make a structure like {'dan':98, 'ang':91, 'kate':78}

#sol1
# final_grades = zip(students, [max(midterms[i], finals[i]) for i in range(len(midterms))])
# print(dict(final_grades))

#sol2
# final_grades = {t[0]:max(t[1],t[2]) for t in zip(students, midterms, finals)}
# print(final_grades)

#sol3
final_grades = zip(
					students,
					map(
						lambda pair: max(pair),
						zip(midterms, finals)
					)
				)
print(dict(final_grades))

#Exercises
#Interleaving Strings fn : accpets two strings, it should return a new string containing 
#the 2 strings interwoven or zipped together
def interleave(str1, str2):
	return "".join(("".join(zipped) for zipped in zip(str1, str2)))

print(interleave('hi','ha'))	#hhia
print(interleave('aaa','zzz'))	#azazaz

#triple_and_filter fn : accepts a list of nos, filter out every number that is not divisible by 4
#and return a new list where every remaining number is tripled
def triple_and_filter(lst):
	return list(map(lambda x:x*3, filter(lambda x:x % 4 == 0, lst)))
print(triple_and_filter([1,2,3,4]))	#[12]
print(triple_and_filter([6,8,3,4]))	#[24,12]

#extract_full_name fn : accepts a list of dictionaries and return a new list of strings with the
#first and last name keys in each dictionaries concatenated
names = [{'first':'Elie', 'last':'Schopik'}, {'first':'Manisha', 'last':'Gupta'}]
def extract_full_name(dictionary):
	return list(map(lambda x:f"{x['first']} {x['last']}", dictionary))
print(extract_full_name(names))		#['Elie Schopik', 'Manisha Gupta']

