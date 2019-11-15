# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!
with open("fighters.csv") as file:
    data = file.read()
# It just gives a giant sentence like structure
# We have to manually deal with it(split it)

# We can use a great alternative instead of spltting it
# Use reader: lets you iterate over rows of CSV as lists
# Or
# Use dictreader: lets you iterate over rows of CSV as OrderedDicts

# Using reader
from csv import reader
with open("fighters.csv") as file:
	csv_reader = reader(file)
	next(csv_reader)		# ignore the headers
	for fighter in csv_reader:
		# each row is a list

		# print(fighter)
		# ['Ryu', 'Japan', '175']
		# ....
		# ['Zangief', 'Russia', '214']

		# Use index to access data
		print(f"{fighter[0]} is from {fighter[1]}")
		# Ryu is from Japan
		# ...
		# Zangief is from Russia

# print(csv_reader)	# <_csv.reader object at 0x03BADF78>

# We can convert it into a list
with open("fighters.csv") as file:
	csv_reader = reader(file)
	data = list(csv_reader)
print(data)
# [['Name', 'Country', 'Height(in cm)'],...., ['Zangief', 'Russia', '214']]

# Using DictReader
from csv import DictReader
with open("fighters.csv") as file:
	csv_dictreader = DictReader(file)
	for fighter in csv_dictreader:
		# Each row is an OrderedDict!
		print(fighter)
		#{'Name': 'Ryu', 'Country': 'Japan', 'Height(in cm)': '175'}
		# ...
		# {'Name': 'Zangief', 'Country': 'Russia', 'Height(in cm)': '214'}
# print(csv_dictreader)		#<csv.DictReader object at 0x04034610>

# Other Delimiter
# Readers accepts a delimiter kwarg incase your data is not
# separated by (,)
# csv_reader = reader(file, delimiter="|")