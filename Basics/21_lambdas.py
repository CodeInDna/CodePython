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

#any : returns True if any element of the iterable is truthy. If the iterable is empty, returns False
nums = [1,2,3,4,5]
any_odds = any([num % 2 != 0 for num in nums])
print(any_odds)			#True

#Generator Expressions and Using sys.getsizeof