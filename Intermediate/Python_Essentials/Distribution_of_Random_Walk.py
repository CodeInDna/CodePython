# RANDOM WALK (Empire State Building)
# Criteria: Rolling a Dice
# 1, 2 : 1 step downwards
# 3, 4, 5: 1 step forward
# 6: Roll a Die again and move forward by the number on dice
# Here, we will see in 100 iteration, how many steps we have climbed.
# We are making a distribution of Random walk by performing it multiple times.

# import modules
import numpy as np

# seed data
np.random.seed(123)

def getRandomNo():
	return np.random.randint(1, 7)

all_walks = []
for i in range(10):
	random_walk = [0]
	for i in range(100):
		step = random_walk[-1]

		dice_roll = getRandomNo()

		if dice_roll <= 2:
			step = max(0, step - 1)
		elif dice_roll in [3, 4, 5]:
			step += 1
		else:
			step += getRandomNo()

		random_walk.append(step)

	all_walks.append(random_walk[-1])

print(f"Number of Steps Covered in each Random Walk: {all_walks}")

# Show Random Walk
import matplotlib.pyplot as plt
import seaborn as sns
plt.plot(all_walks)
plt.xlabel("Walk Number")
plt.ylabel("Steps Covered")
plt.title("Number of Steps Covered in Each Walk")
plt.show()



