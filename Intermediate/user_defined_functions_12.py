# Docstrings describes what your function does
# Serve documentation for your function
# Placed in the immediate line after the function header
# In between triple double quotes """

# functions without parameters and return***********************
# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = "congratulations" + "!!!"

    # Print shout_word
    print(shout_word)

# Call shout
shout()		# congratulations!!!

# functions with single parameters but no return***********************
# Define the function shout
def shout2(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + "!!!"

    # Print shout_word
    print(shout_word)		

# Call shout
shout2("congratulations")	# congratulations!!!

# functions with single parameters and single return***********************
# Define the function shout
def shout3(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + "!!!"

    # Print shout_word
    return shout_word

# Pass 'congratulations' to shout: yell
yell = shout3('congratulations')		

# Print yell
print(yell)		# congratulations!!!


# NOTE: TUPLES
# Make functions to return multiple values
# Differences between tuples and list
	# Like a list- can contain multiple value but
	# Tuples are immutable unlike list
	# Constructed using parenthesis
#Unpacking tuples into several variables :
	# even_nums = (2,4,6)
	# a,b,c = even_nums

# functions with multiple parameters and single return***********************
# Define shout with parameters word1 and word2
def shout4(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + "!!!"
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + "!!!"
    
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout4("congratulations", "you")

# Print yell
print(yell)		# congratulations!!!you!!!

# functions with multiple parameters and multiple return using tuple***********************
# Define shout with parameters word1 and word2
def shout_all(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + "!!!"
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + "!!!"
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell1, yell2 = shout_all("congratulations", "you")

# Print yell
print(yell1, yell2)		# congratulations!!!you!!!




# Practice Exercise*************************************
# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv("dataset/tweets.csv")

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:
    
    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
       langs_count[entry] += 1 
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)	# {'en': 97, 'et': 1, 'und': 2}




tweets_df = pd.read_csv("dataset/tweets.csv")
# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df,'lang')

# Print the result
print(result)	#{'en': 97, 'et': 1, 'und': 2}
