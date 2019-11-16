from csv import writer, reader, DictWriter, DictReader
with open('cats.csv', "w") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["Name", "Age"])
	csv_writer.writerow(["Blue", 3])
	csv_writer.writerow(["Kitty", 1])

# using nested with statements
with open("fighters.csv") as file:
	csv_reader = reader(file)
	with open("upper_case_fighters.csv", "w") as file:
		csv_writer = writer(file)
		for fighter in csv_reader:
			csv_writer.writerow([s.upper() for s in fighter])

# Other approach, with only 1 file open at a time
with open('fighters.csv') as file:
	csv_reader = reader(file)
	# data converted to list and saved to variable
	fighters = [[s.upper() for s in row] for row in csv_reader]

with open('screaming_fighters.csv', "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)



# Using DictReader and DictWriter
def cm_in_in(cm):
	return int(cm) * 0.393701

with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
	headers = ("Name", "Country", "Height")
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	for f in fighters:
		csv_writer.writerow({
			"Name": f["Name"],
			"Country": f["Country"],
			"Height": cm_in_in(f["Height(in cm)"])
		})
