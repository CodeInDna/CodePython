print("CHALLENGE 01 starts here*****************")
# Create a function valid_paranthesis which accepts a string of paranthesis and determines if the order
# of the paranthesis is valid. valid_paranthesis should reurn true is the string is valid, false if its invalid

def valid_paranthesis(paren):
	i = 0
	count = 0
	while i < len(paren):
		if paren[i] == '(':
			count += 1
		if paren[i] == ')':
			count -= 1
		i += 1
	return count == 0
print(valid_paranthesis(')()))'))	# False
print(valid_paranthesis('('))		# False
print(valid_paranthesis('(())((()()())))'))		# False
print(valid_paranthesis('()()()()'))		# True
print("CHALLENGE 01 ends here*****************")



print("CHALLENGE 02 starts here*****************")
# Create a function reverse_vowels which accepts a string and reverse the vowels in a string.
# Any chars which are not vowels remains at the same place 
def reverse_vowels(str):
	 vowels = 'aeiou'
	 i = 0
	 j = len(str)-1
	 new_string = list(str)
	 while i < j:
	 	if new_string[i].lower() not in vowels:
	 		i += 1
	 	elif new_string[j].lower() not in vowels:
	 		j -= 1
	 	else:
	 		new_string[i], new_string[j] = new_string[j], new_string[i]
	 		i += 1
	 		j -= 1
	 return "".join(new_string)

print(reverse_vowels('Hello'))		# False
print(reverse_vowels('Tomatoes'))	# False
print(reverse_vowels('Reverse vowels in a string'))				# True
print("CHALLENGE 02 ends here*****************")


print("CHALLENGE 03 starts here*****************")
# Create a function three_odd_numbers which accepts a list of numbers and returns True.
# If any three consecutive numbers sum to an odd number.
def three_odd_numbers(list):
	i=0
	while i < len(list)-2:
		sum = 0
		for j in range(i, i+3):
			sum += list[j]
		if sum % 2 != 0:
			return True
		i+=1
	return False
print(three_odd_numbers([1,2,3,4,5]))			# True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0]))	# True
print(three_odd_numbers([5,2,1]))				# False
print("CHALLENGE 03 ends here*****************")


print("CHALLENGE 04 starts here*****************")
# Create a function mode which accepts a list of numbers and returns most frequent number
# in the list of numbers. You can assume that mode will be uniwue
# def mode(list):
# 	max_count = 0 
# 	no = 0
# 	for num in list:
# 		count = list.count(num)
# 		if count > max_count:
# 			max_count = count
# 			no = num
# 	return no

# OR

def mode(coll):
	count = {val: coll.count(val) for val in coll}
	max_count = max(count.values())
	correct_index = list(count.values()).index(max_count)
	return list(count.keys())[correct_index]
print(mode([1,2,3,4,5,2,3,4,5,6,4,3,4,2,2,2,4,3,4,4,2,2,2,2]))			# 2
print("CHALLENGE 04 ends here*****************")

