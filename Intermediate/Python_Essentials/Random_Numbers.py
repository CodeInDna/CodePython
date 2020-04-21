# RANDOM NUMBERS (Empire State Building)
# Criteria: Rolling a Dice
# 1, 2 : 1 step downwards
# 3, 4, 5: 1 step forward
# 6: Roll a Die again and move forward by the number on dice

# import modules
import numpy as np

# seed data
np.random.seed(123)

def getRandomNo():
	return np.random.randint(1, 7)

# start at step 50
step = 50
# Roll a Dice
dice_roll = getRandomNo()
if dice_roll <= 2:
	step -= 1
elif dice_roll in [3, 4, 5]:
	step += 1
else:
	step += getRandomNo()

print(step)



