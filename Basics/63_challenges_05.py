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

