#---------------tuple-----------------#
#It is just like a list with one change i.e it is immutable ( safer from bugs, faster than list)
alphabet = ('a','b', 'c', 'd')
type(alphabet)	#tuple
# alphabet[0] = 'm' #typeerror

#defing tuple
months = ('January', 'February', 'March', 'April', 'May')

#accessing tuple
print(months[2])
print(months[-1])

#tuples can be used as keys in dictionaries (list cannot)
locations = {
	(35.3434, 65.4342) : "Tokyo office",
	(343.3434, 6535.4342) : "New York office",
	(325.3434, 656.4342) : "San Francisco office",
}
print(locations[(35.3434, 65.4342)])

#iterating over tuples
for month in months:
	print(month)

i = len(months)-1
while i >= 0:
	print(months[i])
	i -= 1

#tuple method 
#count(returns the number of times a value appears in a tuple)
x = (1,2,3,3,4,5)
print(x.count(3))	#2

#index(returns the index at which a value is found in a tuple)
print(x.index(5))

