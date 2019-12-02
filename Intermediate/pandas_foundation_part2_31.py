# $$$$$$$$$$$$$$ pandas line plots $$$$$$$$$$$$$$$$
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('dataset/file_clean_02.csv')

# Create a list of y-axis column names: y_columns
y_columns = ['AAPL', 'IBM']

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()

# $$$$$$$$$$$$$$ pandas scatter plots $$$$$$$$$$$$$$$$
# The size of each circle is provided as a NumPy array called sizes. This 
# array contains the normalized 'weight' of each automobile in the dataset.
df = pd.read_csv('dataset/auto-mpg.csv')
sizes = pd.read_csv('dataset/sizes.csv')
sizes = np.array(sizes)
# Generate a scatter plot
df.plot(kind='scatter', x='hp', y='mpg', s=sizes)

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()
# Note: automobiles with higher horsepower are less fuel efficient.


# $$$$$$$$$$$$$$ pandas box plots $$$$$$$$$$$$$$$$
# While pandas can plot multiple columns of data in a single figure, making 
# plots that share the same x and y axes, there are cases where two columns 
# cannot be plotted together because their units do not match. The .plot() 
# method can generate subplots for each column being plotted. Here, each plot 
# will be scaled independently.
# Make a list of the column names to be plotted: cols
cols = ['weight', 'mpg']

# Generate the box plots
df[cols].plot(subplots=True, kind="box")

# Display the plot
plt.show()


# $$$$$$$$$$$$$$ pandas hist, pdf and cdf $$$$$$$$$$$$$$$$
# Pandas relies on the .hist() method to not only generate histograms, but also plots of 
# probability density functions (PDFs) and cumulative density functions (CDFs).
df = pd.read_csv('dataset/tips2.csv')

# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', bins=30, density=True, range=(0,.3))
# plt.show()

# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', bins=30, cumulative=True, range=(0,.3))
plt.show()


# $$$$$$$$$$$$$$ Bachelor's degrees awarded to women $$$$$$$$$$$$$$$$
df = pd.read_csv('dataset/percent-bachelors-degrees-women-usa.csv')
# Print the minimum value of the Engineering column
print(df['Engineering'].min())

# Print the maximum value of the Engineering column
print(df['Engineering'].max())

# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')

# Plot the average percentage per year
mean.plot()

# Display the plot
plt.show()

# $$$$$$$$$$$$$$ Median vs mean $$$$$$$$$$$$$$$$
df = pd.read_csv('dataset/titanic.csv')

# Print summary statistics of the fare column with .describe()
print(df['Fare'].describe())

# Generate a box plot of the fare column
df['Fare'].plot(kind='box')

# Show the plot
plt.show()


# $$$$$$$$$$$$$$ Quatiles $$$$$$$$$$$$$$$$
df = pd.read_csv('dataset/Gapminder01.csv')
# First, you will determine the number of countries reported in 2015. There 
# are a total of 260 unique countries in the entire dataset. Then, you 
# will compute the 5th and 95th percentiles of life expectancy over the 
# entire dataset. Finally, you will make a box plot of life expectancy 
# every 50 years from 1800 to 2000. 

# Print the number of countries reported in 2015
print(df['2015'].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05, 0.95]))

# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()


# $$$$$$$$$$$$$$ Separate and summarize $$$$$$$$$$$$$$$$
# Let's use population filtering to determine how the automobiles in the US 
# differ from the global average and standard deviation. How does the distribution 
# of fuel efficiency (MPG) for the US differ from the global average and 
# standard deviation?
df = pd.read_csv('dataset/auto-mpg.csv')
# Compute the global mean and global standard deviation: global_mean, global_std
global_mean = df.mean()
global_std = df.std()

# Filter the US population from the origin column: us
us = df[df['origin'] == 'US']

# Compute the US mean and US standard deviation: us_mean, us_std
us_mean = us.mean()
us_std = us.std()

# Print the differences
print(us_mean - global_mean)
print(us_std - global_std)


# $$$$$$$$$$$$$$ Separate and plot $$$$$$$$$$$$$$$$
# Population filtering can be used alongside plotting to quickly determine 
# differences in distributions between the sub-populations.
# There were three passenger classes on the Titanic, and passengers in each 
# class paid a different fare price. 
titanic = pd.read_csv('dataset/titanic.csv')
# Display the box plots on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# Generate a box plot of the fare prices for the First passenger class
titanic.loc[titanic['Pclass'] == 1].plot(ax=axes[0], y='Fare', kind='box')

# Generate a box plot of the fare prices for the Second passenger class
titanic.loc[titanic['Pclass'] == 2].plot(ax=axes[1], y='Fare', kind='box')

# Generate a box plot of the fare prices for the Third passenger class
titanic.loc[titanic['Pclass'] == 3].plot(ax=axes[2], y='Fare', kind='box')

# Display the plot
plt.show()
# Note: Unsurprisingly, passengers in the first class had the highest fare.
