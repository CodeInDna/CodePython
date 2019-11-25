# Common Data Problems
# * Inconsistent column names
# * Missing Data
# * Outliers
# * Duplicate rows
# * Untidy
# * Need to process columns
# * Columns types can signal unexpected data values

# $$$$$$$$$$$ Loading and viewing your data $$$$$$$$$$$$$
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dataset/dob_job_application_filings_subset.csv')

# Print the head of df
# print(df.head())

# Print the tail of df
# print(df.tail())

# Print the shape of df
# print(df.shape)			# (12846, 82)

# Print the columns of df
# print(df.columns)

print(df['Street Frontage'])	# This column has 0 values, perhaps the data is missing



# $$$$$$$$$$$ Further diagnosis $$$$$$$$$$$$$
# The .info() method provides important information about a DataFrame, 
# such as the number of rows, number of columns, number of non-missing 
# values in each column, and the data type stored in each column. 
# This is the kind of information that will allow you to confirm whether 
# the 'Initial Cost' and 'Total Est. Fee' columns are numeric or strings.
# Print the info of df
print(df.info())
# Notice: that the columns 'Initial Cost' and 'Total Est. Fee' are of 
# type object. The currency sign in the beginning of each value in 
# these columns needs to be removed, and the columns need to be 
# converted to numeric. In the full DataFrame, note that there are a 
# lot of missing values. You saw in the previous exercise that there 
# are also a lot of 0 values. Given the amount of data that is missing 
# in the full dataset, it's highly likely that these 0 values represent 
# missing data.


# $$$$$$$$$$$ Exploratory data analysis $$$$$$$$$$$$$

# $$$$$$$$$$$ Calculating Summary Statistics $$$$$$$$$$$$$
# the .describe() method to calculate summary statistics of your data.
# .describe() can only be used on numeric columns
print(df.describe())


# $$$$$$$$$$$ Frequency Counts $$$$$$$$$$$ 
# So you can diagnose data issues when you have categorical data by 
# using the .value_counts() method, which returns the frequency counts 
# for each unique value in a column!
# This method also has an optional parameter called dropna which is True 
# by default. What this means is if you have missing data in a column, it 
# will not give a frequency count of them. You want to set the dropna column 
# to False so if there are missing values in a column, it will give you the 
# frequency counts.
# Print the value counts for 'Borough'
# print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
# print(df.State.value_counts(dropna=False))

# Print the value counts for 'Site Fill'
# print(df['Site Fill'].value_counts(dropna=False))
# Notice: how not all values in the 'State' column are NY. This is an 
# interesting find, as this data is supposed to consist of applications 
# filed in NYC. Curiously, all the 'Borough' values are correct. A good 
# start as to why this may be the case would be to find and look at the 
# codebook for this dataset. Also, for the 'Site Fill' column, you may 
# r may not need to recode the NOT APPLICABLE values to NaN in your 
# final analysis.


# $$$$$$$$$$$ Data Visualization $$$$$$$$$$$ 
# * Great way to spot outliners and obvious errors
# * More than just looking for patterns
# * Plan data cleaning steps

# $$$$$$$$$$$ Visualizing single variables with histograms $$$$$$$$$$$ 
# * The .plot() method allows you to create a plot of each column of a 
# DataFrame. The kind parameter allows you to specify the type of plot 
# to use - kind='hist', for example, plots a histogram.
# * there are extremely large differences between the min and max values, 
# and the plot will need to be adjusted accordingly. In such cases, it's 
# good to look at the plot on a log scale. The keyword arguments logx=True 
# or logy=True can be passed in to .plot() depending on which axis you 
# want to rescale.Rotate the axis labels by 70 degrees and use a log scale for both axes.
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Describe the column
# print(df['Existing Zoning Sqft'].describe())

# Plot the histogram
# df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
# plt.show()
# Notice: You expected a large amount of counts on the left side of the plot 
# because the 25th, 50th, and 75th percentiles have a value of 0. The 
# plot shows us that there are barely any counts near the max value, 
# signifying an outlier.

# $$$$$$$$$$$ Visualizing multiple variables with boxplots $$$$$$$$$$$ 
# Histograms are great ways of visualizing single variables. To visualize multiple variables, 
# boxplots are useful, especially when one of the variables is categorical.
# We can compare the 'initial_cost' across the different values of the 'Borough' column
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
df.boxplot(column='initial_cost', by='Borough', rot=90)
plt.show()
# Notice: You can see the 2 extreme outliers are in the borough of Manhattan. 
# An initial guess could be that since land in Manhattan is extremely 
# expensive, these outliers may be valid data points. Again, further 
# investigation is needed to determine whether or not you can drop or 
# keep those points in your data.

# $$$$$$$$$$$ Visualizing multiple variables with scatter plots $$$$$$$$$$$ 
# Boxplots are great when you have a numeric column that you want to 
# compare across different categories. When you want to visualize two 
# numeric columns, scatter plots are ideal.
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
# df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
# plt.show()

# Notice: In general, from the second plot it seems like there is a strong 
# correlation between 'initial_cost' and 'total_est_fee'. In addition, 
# take note of the large number of points that have an 'initial_cost' 
# of 0. It is difficult to infer any trends from the first plot 
# because it is dominated by the outliers.


# $$$$$$$$$$$ Tidy Data $$$$$$$$$$$ 
# * Colums represent separate variables
# * Rows represent individual observations
# * Observational units form tables