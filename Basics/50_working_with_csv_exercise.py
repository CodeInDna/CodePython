# We are working with users.csv file

import csv
# add_users: takes in first name and last name and adds a new user to the users,csv file
def add_users(first_name, last_name):
	with open("users.csv", "a") as file:
		csv_writer = csv.writer(file)
		csv_writer.writerow([first_name, last_name])
# add_users("Chinky", "Jain")

# print_users: prints out all of the first and last names in users.csv
def print_users():
	with open("users.csv") as csvfile:
		csv_reader = csv.DictReader(csvfile)
		for row in csv_reader:
			print(f"{row['FirstName']}, {row['LastName']}")
# print_users()


# find_user: Takes in a first name and last name and searches for a user with that first name
# and last name in the users.csv file. If the user is found, return the index where the user is found,
# Otherwise it returns a message stating that the user wasn't found.
# Note: enumerate function bind the values with index in tuples
def find_user(first_name, last_name):
	with open("users.csv") as file:
		csv_reader = csv.reader(file)
		for (index, row) in enumerate(csv_reader):
			if row[0] == first_name and row[1] == last_name:
				return index
		return f"{first_name} {last_name} not found"

# print(find_user("Shakira","Henz"))	#1
# print(find_user("No","One"))		#No One not found


# update_user: Takes in an old first name, an old last name, a new first name and a new last name
# Update the users.csv file so that any user whose first and last names match the old first and last 
# names are updated to the new first and last names. The function should retuurn a count of how many users are updated.
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
        return f"{count}"
# print(update_users("Shakira","Henz","Shaku", "Devi"))


# delete_users: Takes in a first_name and a last_name. Updates the user.csv file so 
# that any user whose first and last names matches the inputs are removes. The 
# function should return a count of how many users were removed
def delete_users(fname, lname):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == fname and row[1] == lname:
                count += 1
            else:
                csv_writer.writerow(row)
        return f"Users Deleted: {count}"
# print(delete_users("Shakira","Henz"))       #Users Deleted: 2
				