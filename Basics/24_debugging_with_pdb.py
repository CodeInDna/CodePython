#--------------debugging with pdb--------------#
# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)

def add(a,b):
	import pdb; pdb.set_trace()
	return a+b
print(add(4,5))

#import pdb
#pdb.set_trace()

#Also commonly on one line:
#import pdb; pdb.set_trace()

#common pdb commands
# l (list)
# n (next line)
# p (print - prints the variable value if variable name is similar to pdb commands)
# c (continue - finishes debugging)