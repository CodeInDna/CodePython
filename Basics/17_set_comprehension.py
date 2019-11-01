#---------------sets comprehension-----------------#
items = {x**2 for x in range(10)} #dictionary -> {x:x**2 for x in range(10)}
print(items)

string = 'hello'
vowels = {char for char in string if char in 'aeiou'}
print(vowels)	#{'o','e'}
length = len({char for char in string if char in 'aeiou'}) == 5
print(length) #False