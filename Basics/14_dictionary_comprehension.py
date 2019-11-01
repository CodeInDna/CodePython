#----------dictionary comprehension------------#
numbers = dict(first=1, second=2, third=3)
squared_nos = {k: v ** 2 for k,v in numbers.items()}
print(squared_nos)

dict_from_list = {num: num**2 for num in [1,2,3,4,5]}
print(dict_from_list)

str1 = 'ABC'
str2 = "123"
combo = {str1[pair]: str2[pair] for pair in range(0, len(str1))}
print(combo)

teacher = {'name':'vimi', 'age':'40', 'strict':'yes'}
upper_teacher = {k.upper() : v.upper() for k,v in teacher.items()}
print(upper_teacher)

#conditional logic
num_list = [1,2,3,4,5]
num_list_final = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(num_list_final)


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer = {list1[i]: list2[i] for i in range(0, len(list2))}
print(answer)

person = [["name", "Jersey"], ["job", "Musician"], ["city", "Bern"]]
result = {person[i][0]: person[i][1] for i in range(0, len(person))}
# result = {item[0]: item[1] for item in person}
# result = {k:v for k,v in person}
# result = dict(person)
print(result)

res = {alpha_num: 0 for alpha_num in 'aeiou'}
# res = dict.fromkeys('aeiou', 0)
print(res)

asci = {char: chr(char) for char in range(65, 91)}
print(asci)