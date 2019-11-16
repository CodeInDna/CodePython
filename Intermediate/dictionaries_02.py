#-------------Dictionaries---------------------#
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')	#2

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])	#berlin


# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())	# dict_keys(['france', 'spain', 'norway', 'germany'])

# Print out value that belongs to key 'norway'
print(europe['norway'])	# oslo


# Adding key-value pair to dictionaries-----------------------------
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)	#True

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)	#{'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw'}


# Updation and Deletion
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin' 


# Remove australia
del(europe['australia'])

# Print europe
print(europe)	#{'italy': 'rome', 'norway': 'oslo', 'germany': 'berlin', 'poland': 'warsaw', 'france': 'paris', 'spain': 'madrid'}


# Multidimensional dictionary
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])	# paris

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)
# {'france': {'capital': 'paris', 'population': 66.03}, 
# 'spain': {'capital': 'madrid', 'population': 46.77}, 
# 'norway': {'capital': 'oslo', 'population': 5.084}, 
# 'germany': {'capital': 'berlin', 'population': 80.62}, 
# 'italy': {'capital': 'rome', 'population': 59.83}}