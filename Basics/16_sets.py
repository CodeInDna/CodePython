#---------------sets-----------------#
#elements in sets do not have order(like dictionary), cannot have duplicates and do not have keys (like list)

#creating / accessing
s = set({1,2,3,4,5,5,5,5})		#cannot have duplicates
print(s)	# {1,2,3,4,5}

# print(s[0])	# Typeerror (no indexing)

for num in s:
	print(num)

months = ['January', 'February', 'March', 'April', 'May', 'May']
print(list(set(months)))	#give the list of unique month
print(len(set(months)))		#give the length of unique month


#set methods
# add
s.add(9)
print(s)

#remove
s.remove(5)
print(s)

s.discard(7)	#does not throw error even if the item is not present in the set otherwise remove the item
print(s)

#copy
another_s = s.copy()
print(another_s)

#clear
another_s.clear()
print(another_s)

#set math
list1 = {1,2,3,4,5}
list2 = {1,2,6,7,8}
union = list1 | list2	#union (unique items from both the list)
intersection = list1 & list2	#intersection (common items from both the list)
print(union)
print(intersection)