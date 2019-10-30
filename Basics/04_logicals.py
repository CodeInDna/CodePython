# Logical AND
num = 10
if num < 12 and num > 8:
	print("Under the boundaries")
else:
	print("Outside the boundaries")

# Logical OR
food = input('What is your favorite food (apple, grape, bacon, steak, worm, dirt)')

if food == 'apple' or food == 'grape':
	print('Fruit')
elif food == 'bacon' or food == 'steak':
	print('meat')
elif food == 'dirt' or food == 'worm':
	print('yukk')

# Logical NOT
age = 2
#2-8 2 dollar ticket
#65 5 dollar ticket
#10 dollars for everyone else

if not ((age >= 2 and age <= 8) or age >= 65):
	print('10 Dollars')
else:
	print('Pay 2 or 8 Dollars')