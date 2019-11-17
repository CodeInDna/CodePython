# Randomness has many uses in science, art, statistics, cryptography, gaming, gambling, and other fields. You're going to use randomness to simulate a game.

# All the functionality you need is contained in the random package, a sub-package of numpy. In this exercise, you'll be using two functions from this package:

# seed(): sets the random seed, so that your results are reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
# rand(): if you don't specify any arguments, it generates a random float between zero and one.

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# randint(4,8), also a function of the random package, to generate 
# integers randomly. The following call generates the integer 4, 5, 6 or 7 randomly. 8 is not included.
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))


# Roll the dice. Use randint() to create the variable dice.
# If dice is 1 or 2, you go one step down.
# if dice is 3, 4 or 5, you go one step up.
# Else, you throw the dice again. The number of eyes is the number of steps you go up.
# Starting step
np.random.seed(123)
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice < 6 :
    step += 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step)	#6 53


# Make a list random_walk that contains the first step, which is the integer 0.
# Finish the for loop:
# The loop should run 100 times.
# On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
# Next, let the if-elif-else construct update step for you.
# The code that appends step to random_walk is already coded.
# Print out random_walk.
# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)
    # print(dice)
    # Determine next step
    if dice <= 2:
        step = max(0, step - 1)	# So that step doesnt go below 0
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

# Simulate multiple walks
# A single random walk is one thing, but that doesn't tell you 
# if you have a good chance at winning the bet.
# To get an idea about how big your chances are of reaching 60 steps, 
# you can repeatedly simulate the random walk and collect the results.
# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(250) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
# print(all_walks)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()