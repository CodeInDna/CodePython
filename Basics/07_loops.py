# ####### for loops #######
from random import randint
# print("***************************************")
# print("************** FOR LOOP ***************")
# print("***************************************")
# print("******* Print nos from 1 to 9 *********")
# for x in range(1, 10):
# 	print(x)			# prints 1 to 9

# print("*********** Print letters *************")
# for letter in 'coffee':
# 	print(letter*10)	#print every letter in "coffee" 10 times

# for num in range(10,0,-1):	#print 10 to 1 (exclude 0)
# 	print(num)

# print("************* Sum up odds *************")
# # Sum the odd nos between 11 and 20
# sum_odd = 0
# for odd in range(11, 20, 2):
# 	sum_odd+=odd
# print(sum_odd)

# print("********** Get user inputs *************")
# # Print the line as many times as user say
# repeat = input("How many times do I have to tell you?")
# for times in range(int(repeat)):
# 	print(f"Time {times+1} CLEAN UP YOUR ROOM!")

# print("*********** Unlucky Numbers ************")
# # Print 4 and 13 as unlucky, while classify remaining no's as odd or even
# for num in range(1, 21):
# 	if num == 4 or num == 13:
# 		status = 'UNLUCKY'
# 	elif num % 2 == 0:
# 		status = 'even'
# 	else:
# 		status = 'odd'
# 	print(f"{num} is {status}")

# ####### while loops #######
# print("****************************************")
# print("************* WHILE LOOP ***************")
# print("****************************************")
# print("*********** Secret Password ************")
# msg = input("whats the secret Password? ")
# while msg != 'secret':
# 	print("WRONG! Try Again!")
# 	msg = input("whats the secret Password? ")
# print("CORRECT!")


# print("******* Print nos from 1 to 9 *********")
# num = 1	
# while num < 10:		# prints 1 to 9
# 	print(num)
# 	num += 1

# print("************* Pyramid Art **************") 
# print("************ Using for loop ************") 
# for num in range(1, 11):
# 	print("*" * num)

# print("***********Using while loop ************") 
# n = 1
# while n <= 10:
# 	print('*' * n)
# 	n += 1

# print("***********Using for & while************") 
# for num in range(1,11):
# 	count = 1
# 	star = ''
# 	while count <= num:
# 		star += '*'
# 		count += 1
# 	print(star)

# print("************Stop copying me*************") 
# reply = input('How\'s it going? ')
# while reply != 'stop copying me':
# 	reply = input(f'{reply}\n ')
# print('UGHHHHH, You Win!')

print("************* Exercise *****************") 
rand_num = 0 #store random number in here, each time through
i = 0		# i should be incremented by one each iteration
while rand_num != 5:	 #keep looping while number is not 5
	i += 1
	rand_num = randint(1,10)	#update number to be a new random int from 1-10
print(i)