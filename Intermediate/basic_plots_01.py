#------------Intermediate Python---------------#
# Data Visualization 

# Basic Plots with Matplotlib(a package)
# With matplotlib, we can create a bunch of different plots in Python. 
# The most basic plot is the line plot. 
# pyplot is a subset of matplotlib

import matplotlib.pyplot as plt
import numpy as np
from world_development import gdp_cap, life_exp, pop, col

# plot the line graph
# plt.plot(gdp_cap, life_exp)

# show the linegraph
# plt.show()

# plot the scatter graph
# plt.scatter(gdp_cap, life_exp)  # year : x-axis, pop : y-axis
# 3rd Argument : size of the dots(set it to the size of population)
# 4th Argument : color of the dots
# 5th Argument : Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent.
np_pop = np.array(pop) * 2
plt.scatter(gdp_cap, life_exp, s = np_pop, c = col, alpha = 0.5)  # year : x-axis, pop : y-axis

# Put the x-axis on a logarithmic scale
plt.xscale('log')		# We can use this if we have large amount of data(for good visualization)

# plot labels and title
plt.xlabel('GDP per capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title("World's Population in 2007")

# tick values(x-axis)
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
plt.xticks(tick_val, tick_lab)

# Add text at some coordinates
plt.text(1550, 71, 'India')
plt.text(5770, 80, 'China')

# Add grid (graph background)
plt.grid(True)

# show the scatter graph
plt.show()

# Conclusion : it's clear that people live longer in countries 
# with a higher GDP per capita. No high income countries have really 
# short life expectancy, and no low income countries have very long 
# life expectancy. Still, there is a huge difference in life expectancy
# between countries on the same income level. Most people live in middle 
# income countries where difference in lifespan is huge between countries;
# depending on how income is distributed and how it is used.

