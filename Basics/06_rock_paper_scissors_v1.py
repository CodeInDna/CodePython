#-----------------------Rock Paper Scissor Game-------------------------#
print('***************ROCK*****************')
print('***************PAPER****************')
print('*************SCISSORS***************')

######### IMPROVED VERSION ###########

from random import randint	# OR import random
rand_num = randint(0,2)		# OR random.randint
if rand_num == 0:
	computer = 'rock'
elif rand_num == 1:
	computer = 'paper'
else:
	computer = 'scissors'

player = input("Player, make your move : ").lower()
print(f"Computer plays {computer}")

if player == computer:
	print('It\'s a TIE.')
elif player == 'rock':
	if computer == 'scissors':
		print('Player wins')
	else:
		print('Computer wins')
elif player == 'paper':
	if computer == 'rock':
		print('Player wins')
	else:
		print('Computer wins')
elif player == 'scissors':
	if computer == 'paper':
		print('Player wins')
	else:
		print('Computer wins')		
else:
	print('Invalid input!')



######### INTERMEDIATE VERSION ###########

# player1 = input("Player 1, make your move : ")
# print('*****NO CHEATING !*****\n\n' * 22)
# player2 = input("Player 2, make your move : ")

# if player1 == player2:
# 	print('It\'s a TIE.')
# elif player1 == 'rock':
# 	if player2 == 'scissors':
# 		print('Player 1 wins')
# 	elif player2 == 'paper':
# 		print('Player 2 wins')
# elif player1 == 'paper':
# 	if player2 == 'rock':
# 		print('Player 1 wins')
# 	elif player2 == 'scissors':
# 		print('Player 2 wins')
# elif player1 == 'scissors':
# 	if player2 == 'paper':
# 		print('Player 1 wins')
# 	elif player2 == 'rock':
# 		print('Player 2 wins')		
# else:
# 	print('Invalid input!')



######### BASIC VERSION ###########

# if player1 == 'rock' and player2 == 'scissors':
# 	print('Player 1 wins')
# elif player1 == 'rock' and player2 == 'paper':
# 	print('Player 2 wins')
# elif player1 == 'paper' and player2 == 'rock':
# 	print('Player 1 wins')
# elif player1 == 'paper' and player2 == 'scissors':
# 	print('Player 2 wins')
# elif player1 == 'scissors' and player2 == 'paper':
# 	print('Player 1 wins')
# elif player1 == 'scissors' and player2 == 'rock':
# 	print('Player 2 wins')
# elif player1 == player2:
# 	print('It\'s a TIE.')
# else:
# 	print('Invalid input!')
