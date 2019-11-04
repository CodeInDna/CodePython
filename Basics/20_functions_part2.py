#------------functions part 2--------------#
# *args (it can be named anything like *nums) operator (it is used to pass a variable 
# number of arguments to a fn)
# In the below example, it treat the first param as num1 and rest of them treated
# as the list of tuples 
def sum_nums(num1, *args):
	print(num1)		#3
	total = 0
	for nums in args:
		total += nums
	return total
print(sum_nums(3,4,5,7,8,0,2,3,4))		#33 (4+5+7+8+0+2+3+4)


# **kwargs (A special operator we can pass to fn, gathers remaining keywords arguments as a dictionary)
def fav_colors(**kwargs):
	# return (kwargs)
	for person, color in kwargs.items():
		print(f"{person} favourite color is : {color}")
fav_colors(emmel="red",jina="black",simba="white")

# parameter ordering (Important to remember the ordering)
# 1. parameters
# 2. *args
# 3. default paramters
# 4. **kwargs
def display_info(a, b, *args, instructor="Pummy", **kwargs):
	return [a,b, args, instructor, kwargs]
print(display_info(1,2,3, last_name="Doe", job="Teacher"))		#[1, 2, (3,), 'Pummy', {'last_name': 'Doe', 'job': 'Teacher'}]
# a = 1
# b = 2 
# args = (3,)
# instructor = "Pummy"
# kwargs = {'last_name':"Doe", 'job':"Teacher"} 


# tuple unpacking(*) (adding * when passing list as an argument) 
# **************error error error********************#
# def sum_all_values(*args):
# 	print(args)		#([1,2,3,4,5,6],)
# 	total = 0
# 	for num in args:
# 		total += num
# 	print(total)
# nums = [1,2,3,4,5,6]
# print(sum_all_values(nums))	#as argument is a list, it will throw an error 
# **************error error error********************#


def sum_all_values2(*args):
	print(args)		#([1,2,3,4,5,6],)
	total = 0
	for num in args:
		total += num
	return total
nums = [1,2,3,4,5,6]
print(sum_all_values2(*nums))	#*num - unpack the list 


# Dictionary Unpacking(adding ** when passing dictionary as an argument) 
def fav_colors2(**kwargs):
	for person, color in kwargs.items():
		print(f"{person} favourite color is : {color}")

details = {"emmel":"red","jina":"black","simba":"white"}
fav_colors2(**details)


#Exercises
# *args Exercise: The Purple Test
# contains_purple : accepts any no of args, should return True if any of the args are "purple" 
# otherwise returns False
def contains_purple(*args):
	if "purple" in args:
		return True
	return False
print(contains_purple(25, "purple"))		#True
print(contains_purple("green", False, 37, "blue", "hello world"))	#False
print(contains_purple("purple"))			#True
print(contains_purple("a", 99, "blah blah blah", 1, True, False, "purple"))	#True
print(contains_purple(1,2,3))				#False


# **kwargs Exercise: Combine Words
# combine_words : accepts single word and any no of additional key word args 
# if the prefix is provided, return prefix followed by the word
# if the suffix is provided, return the word followed by the suffix
# if neither is provided, just return the word 
def combine_words(word, **pre_or_suff):
	if 'prefix' in pre_or_suff:
		return f"{pre_or_suff['prefix']}{word}"
	elif 'suffix' in pre_or_suff:
		return f"{word}{pre_or_suff['suffix']}"
	return word
print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))
print(combine_words("work", suffix="er"))
print(combine_words("work", prefix="home"))


# *Unpacking Exercise: Count Sevens
def count_sevens(*args):
	return args.count(7)
nums = [90,34,2,7,4,2,1,4,7,34,23,2,4,5,7,8,7,8,5,7,5,6,4,5,7,5,7,6,7,8,9,8,6,7,8,7,6,4,6,7,8,8,67,7]

result1 = count_sevens(1,4,7)
result2 = count_sevens(*nums)
print(result1)
print(result2)

#calculate
def calculate(**kwargs):
	operation_lookup = {
		'add': kwargs.get('first', 0) + kwargs.get('second', 0),
		'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
		'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
		'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
	}
	is_float = kwargs.get('make_float', False)
	operation_val = operation_lookup[kwargs.get('operation', '')]
	if is_float:
		final = f"{kwargs.get('message', 'The result is ')}{float(operation_val)}"
	else:
		final = f"{kwargs.get('message', 'The result is ')}{int(operation_val)}"
	return final
print(calculate(make_float=False, operation='add',message='You just added ',first=1,second=2))
print(calculate(make_float=True, operation='divide',first=3.5,second=5))

