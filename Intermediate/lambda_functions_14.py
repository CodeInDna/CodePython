# Normal Function Example
def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words

# Converting it to lambda function
# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)		#heyheyheyheyhey


# The best use case for lambda functions, however, are for when 
# you want these simple functionalities to be anonymously embedded
# within larger expressions. What that means is that the functionality 
# is not stored in the environment, unlike a function defined with def.
# To understand this idea better, we will use a lambda function in 
# the context of the map() function.
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item+"!!!", spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Print the result
print(shout_spells_list)	# ['protego!!!', 'accio!!!', 'expecto patronum!!!', 'legilimens!!!']

# Another Example with filter()
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)		# ['samwise', 'aragorn', 'boromir', 'legolas', 'gandalf']


# Another Example with reduce()
# The reduce() function is useful for performing some computation on 
# a list and, unlike map() and filter(), returns a single value as a result. 
# To use reduce(), we must import it from the functools module.
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce((lambda item1, item2: item1 + item2), stark)

# Print the result
print(result)		# robbsansaaryabrandonrickon