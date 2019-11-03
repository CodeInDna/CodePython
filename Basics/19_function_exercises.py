#multiply : fn to return the product of two nos
def multiply(a, b):
	return a * b
print(multiply(2,2))
print(multiply(2,-2))


#return_day : fn to get day by passing a number (1:sunday, 2:monday & so on)
# def return_day(num):
# 	days = {1 : "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday" }
# 	day = days.get(num)	#get() return None when invalid num is passed
# 	return day
# print(return_day(8))

# OR
def return_day(num):
	days = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
	if num > 0 and num <= len(days):
		return days[num-1]
	return None
print(return_day(3))


#last_element : takes in one parameter(a list) and return th last value in the list
def last_element(li):
	if li: 
		return li[-1]
	return None
print(last_element([1,2,3]))
print(last_element([]))

#number_compare : takes in two param(nos) and tells which one is greater otherwise both are equal
def number_compare(num1, num2):
	if num1 > num2:
		return 'First is Greater! '
	elif num1 < num2:
		return 'Second is Greater! '
	return 'Numbers are Equal! '
print(number_compare(3,6))
print(number_compare(3,3))

#single_letter_count : takes 2 params, a word and a letter. fn should return the no of times letter is appears in the word(case insensitive)
# def single_letter_count(word, letter):
# 	count = 0
# 	for l in word:
# 		if letter.lower() == l.lower():
# 			count += 1
# 	return count
# print(single_letter_count("Hello World", "a"))

# OR

def single_letter_count(word, letter):
	return word.lower().count(letter.lower())
print(single_letter_count("Hello World", "a"))


#multiple_letter_count : takes in 1 param(string) & returns a dict with keys being the letters and values being the count of the letter
def multiple_letter_count(word):
	return {l:word.lower().count(l.lower()) for l in word }
print(multiple_letter_count("awesome"))


#list_manpualtion : takes 4 param(list, command, location, value)
def list_manipulation(li, comm, loc, val = 0):
	if comm == 'remove' and loc == 'end':
		return li.pop()	#remove from the end
	elif comm == 'remove' and loc == 'beginning':
		return li.pop(0)	#remove from the beginning
	elif comm == 'add' and loc == 'beginning':
		li.insert(0, val)	#add item to the beginning
		return li
	elif comm == 'add' and loc == 'end':
		li.append(val)	#add item to the end
		return li

print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "add", "beginning", 3))
print(list_manipulation([1,2,3], "add", "end", 5))


#is_palindrome : take in one param & return True or False depending on whether it is palindrome or not
def is_palindrome(string):
	stripped = string.replace(" ", "")	#remove space
	return stripped == stripped[::-1]	#reverse string and compare
print(is_palindrome("sms"))
print(is_palindrome("Not_Palindrome"))


#frequency : takes in a list and a search term and returns the no of times search_term appears in the list
def frequency(li, to_search):
	return li.count(to_search)
print(frequency([1,2,3,4,5,5,4,4], 4))
print(frequency([True, False, True, True, False], False))

#multiply_even_numbers : accepts a list of nos and return the product of all even nos
def multiply_even_numbers(li):
	sum = 1
	for num in li:
		if num % 2 == 0:
			sum *= num
	return sum
print(multiply_even_numbers([1,2,3,4,5,6,7,8,9]))

#capitalize : accepts a string and return the same string with the first letter capital
def capitalize(str):
	return str[0].upper() + str[1:]
print(capitalize("jamaica"))
		 

#compact : accepts a list and return a list of values that are truthy, without any falsy values
def compact(li):
	truthy_vals = [val for val in li if val]
	return truthy_vals
print(compact([0,1,2,"",[], False, {}, None, "All done"]))

#intersection : accepts two list and return a list with values that are in both lists
def intersection(li1, li2):
	return [val for val in li1 if val in li2]
	# return [val for val in set(li1) & set(li2)]
print(intersection([1,2,3], [2,3,4]))

#partition : accepts a list and a callback fn
def isEven(num):
	return num % 2 == 0

# def partition(li, callback):
# 	truthy = []
# 	falsy = []
# 	for num in li:
# 		if callback(num):
# 			truthy.append(num)
# 		else:
# 			falsy.append(num)
# 	return [truthy, falsy]
# print(partition([1,2,3,4], isEven))

#Or

def partition(li, callback):
	return [[val for val in li if callback(val)], [val for val in li if not callback(val)]]
print(partition([1,2,3,4], isEven))