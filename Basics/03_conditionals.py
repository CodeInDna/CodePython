#ifs, elifs and else conditional statements
#1) if else 
num = float(input('Enter a number: '))

if num%2 == 0:
	print("Even")
else:
	print("Odd")


#2) if elif and else
color = input('What\'s your favourite color?')

if color == 'blue':
	print('Excellent Choice')
elif color == 'teal':
	print('Not bad')
elif color == 'pink':
	print('Too kidish')
elif color == 'black':
	print('Everyone likes black')
else:
	print('YOU ARE AN ALIEN!')