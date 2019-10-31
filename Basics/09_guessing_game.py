#---------Guessing Game-------------#
#You are provided a range within which you have to guess a number
#After entering a number, it will tell you: 
#1. The guessed number is lower or
#2. The guessed number is higher or
#3. You guessed it right
#After guessing the number right, it will keep asking you whether you want to play again or not until you hit no

from random import randint

#generate a random number as a standard
rand_num = randint(1, 10)	

while True:
	#ask for a number from the user
	number = input("Guess a number between 1 - 10: ")
	number = int(number)

	#tell them if they are too high or too low
	if rand_num > number:
		print('The number is too low, Try Again!')
	elif rand_num < number:
		print('The number is too high, Try Again!')
	#if they guess correct, tell them they won
	else:
		print('You got it right, CONGRATS!!')
		#let them play again if they want
		play_again = input("Do you want to play again (y/n) : ").lower()
		if play_again == 'y':
			rand_num = randint(1,10)
			number = None
		else:
			print("Thank you for playing!")
			break


