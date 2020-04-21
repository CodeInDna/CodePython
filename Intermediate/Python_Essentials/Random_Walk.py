# RANDOM WALK (Empire State Building)
# Criteria: Rolling a Dice
# 1, 2 : 1 step downwards
# 3, 4, 5: 1 step forward
# 6: Roll a Die again and move forward by the number on dice
# Here, we will see in 100 iteration, how many steps we have climbed.

# import modules
import numpy as np

# seed data
np.random.seed(123)

def getRandomNo():
	return np.random.randint(1, 7)

random_walk = [0]
for i in range(100):
	step = random_walk[-1]

	dice_roll = getRandomNo()

	if dice_roll <= 2:
		step -= 1
	elif dice_roll in [3, 4, 5]:
		step += 1
	else:
		step += getRandomNo()

	random_walk.append(step)

print(f"Random Walk: {random_walk}, Steps Covered: {random_walk[-1]}")

# Show Random Walk
import matplotlib.pyplot as plt

plt.plot(random_walk)
plt.xlabel("Iteration Number")
plt.ylabel("Steps Covered")
plt.show()



