#------------list comprehensions--------------#
names = ["Elie", "Tim", "Matt"]
# Basic way to pluck first letter from each item and put them in a list
# first_letter = []
# for name in names:
# 	first_letter.append(name[0])
# print(first_letter)

#Using list comprehension
first_letter = [name[0] for name in names]
print(first_letter)


#---list comprehensions with conditionals-----#
numbers = [1,2,3,4,5,6,7,8]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(evens)
print(odds)


mul_div = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(mul_div)

#remove vowels
with_vowels = "This is so much fun!"
no_vowels = [char for char in with_vowels if char not in 'aeiou']
print(''.join(no_vowels))

#find even nos
nums = [1,2,3,4,5,6]
answer = [num for num in nums if num%2==0]
print(answer)

# find the intersection of both list which is [3,4]
list1 = [1,2,3,4]
list2 = [3,4,5,6]
result = [num for num in list1 if num in list2]
print(result)

#reverse the words, all in lower case
words = ["Elie","Tim","Matt"]
res = [word[::-1].lower() for word in words]
print(res)

#make the list with numbers divisble by 12 between 1 to 100
divisible_by_12 = [num for num in range(1,101) if num % 12 == 0]
print(divisible_by_12)

#exclude vowels from the string
new_word = 'amazing'
no_vowel = [char for char in new_word if char not in 'aeiou']
print(no_vowel)

#nested list
#access items from the nested list
nested_list = [[1,2,3],[2,3,4],[5,6,7]]
print(nested_list[0][1])
print(nested_list[1][-1])

#iterating over nested list
coords = [[10.423], [37.212, -14.092], [21.343,82.32]]
for loc in coords:
	for val in loc:
		print(val)

#nested list comprehension
[[print(val1) for val1 in loc1] for loc1 in coords]


odd_even = [["X" if val % 2 != 0 else 'O' for val in range(1,4)] for num in range(1,4)]
print(odd_even)

list_of_nums = [[val for val in range(0,3)] for num in range(1,4)]
print(list_of_nums)

matrix_of_10_10 = [[val for val in range(0,10)] for num in range(1,11)]
print(f"{matrix_of_10_10}")