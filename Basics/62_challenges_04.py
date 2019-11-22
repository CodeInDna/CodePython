print("CHALLENGE 01 starts here*****************")
# Create a function reverse_string which accepts a string and return a new string
#with all the char reversed

def reverse_string(str):
	return str[::-1]
print(reverse_string('awesome'))	# emosewa
print(reverse_string('meena'))		# aneem
print(reverse_string('Elie'))		# eilE
print("CHALLENGE 01 ends here*****************")



print("CHALLENGE 02 starts here*****************")
# Create a function list_check which accepts a list and returns True if each value in the list is a list
# Otherwise fn should return False
def list_check(lists):
	 return all(type(lst) == list for lst in lists)
print(list_check([[], [1], [2,3], (1,2)]))		# False
print(list_check([1, True, [], [1], [2,3]]))	# False
print(list_check([[], [1], [2,3]]))				# True
print("CHALLENGE 02 ends here*****************")


print("CHALLENGE 03 starts here*****************")
# Create a function remove_every_other which accepts a list and returns a new list with every second value removed
def remove_every_other(list):
	 return [val for i, val in enumerate(list) if i % 2 == 0]
print(remove_every_other([1,2,3,4,5]))		# [1, 3, 5]
print(remove_every_other([5,1,2,4,1]))		# [5, 2, 1]
print(remove_every_other([1]))				# [1]
print("CHALLENGE 03 ends here*****************")


print("CHALLENGE 04 starts here*****************")
# Create a function sum_pairs which accepts a list and a number returns first air of numbers that
# sum to the number passed to the function
# def sum_pairs(list, number):
# 	for i in range(len(list)-1):
# 		if list[i] + list[i+1] == number:
# 			return [list[i], list[i+1]]
# 		return []
# OR

def sum_pairs(list, number):
	already_visited = set()
	for i in list:
		diff = number - i
		if diff in already_visited:
			return [diff, i]
		already_visited.add(i)
	return []
print(sum_pairs([4,2,10,5,1], 6))			# [4, 2]
print(sum_pairs([11,20,4,2,1,5], 100))		# []
print("CHALLENGE 04 ends here*****************")

print("CHALLENGE 05 starts here*****************")
# Create a function vowel_count which accepts a string and return a dict with keys as the vowels and values
# as the count of times that vowel appears in the string
# def vowel_count(str):
# 	vowel_count = {}
# 	for letter in str.lower():
# 		if letter in 'aeiou':
# 			if letter in vowel_count:
# 				vowel_count[letter] += 1
# 			else:
# 				vowel_count[letter] = 1
# 	return vowel_count

# OR
def vowel_count(str):
	return {letter: str.lower().count(letter) for letter in str.lower() if letter in 'aeiou'}
print(vowel_count('awesome'))	# {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie'))		# {'e': 2, 'i': 1}
print(vowel_count('Meena'))		# {'e': 2, 'a': 1}
print("CHALLENGE 05 ends here*****************")