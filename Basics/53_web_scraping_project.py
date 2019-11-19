# Web Scraping Project: Guess the Author Name - A Guessing Game

# Task 1 **********************************************
# Scrap the quotes, author's name and bio-link from a website "http://quotes.toscrape.com/"
# import necessary modules
import requests
from bs4 import BeautifulSoup
# from time import sleep
from csv import DictReader

# define the url's
BASE_URL = "http://quotes.toscrape.com/"

def read_quotes(filename):
	with open(filename, "r") as file:
		csv_reader = DictReader(file)
		return list(csv_reader)


# Task 2 **********************************************
# Display the quote to the user and ask who said it. The player will have four guesses remaining.
# After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!
# After every incorrect guess, the player receives a hint about the author. 
# For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the player the author's birth date and location.
# The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.
# When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.
# from random import choice
from random import choice

def start_game(quotes):
	quote = choice(quotes)

	print("Here's a quote: ")
	print(quote["text"])

	guesses_rem = 4
	user_input = ''
	while user_input.lower() != quote['author'].lower() and guesses_rem > 0:
		user_input = input(f"\nWho said this? Guesses remaining: {guesses_rem}. ")
		if user_input.lower() == quote['author'].lower():
			print("You guessed it right! CONGRATULATIONS!!!")
			break
		guesses_rem -= 1
		get_hints(quote, guesses_rem)

	play_again = ''
	while play_again.lower() not in ('y', 'n', 'yes', 'no'):
		play_again = input("Would you like to play again (y/n)? ")
		if play_again.lower() in ('yes','y'):
			return start_game(quotes)
		else:
			print("OK, GOODBYE")

def get_hints(quote,guesses_rem):
	if guesses_rem == 3:
			res_auth = requests.get(f"{BASE_URL}{quote['bio_link']}")
			soup_auth = BeautifulSoup(res_auth.text, "html.parser")
			auth_born_date = soup_auth.find(class_="author-born-date").get_text()
			auth_born_place = soup_auth.find(class_="author-born-location").get_text()
			hint1 = f"The author was born in {auth_born_date} {auth_born_place}"
			print(f"Here's a hint: {hint1}") 
	elif guesses_rem == 2:
		hint2 = quote['author'][0]
		print(f"The author's first name starts with {hint2}")
	elif guesses_rem == 1:
		hint3 = quote['author'].split(" ")[1]
		print(f"The author's last name starts with {hint3}")
	else:
		print(f"Sorry, you've run out of guesses. The answer was {quote['author']}")

quotes = read_quotes("quotes.csv")
start_game(quotes)

# def pick_a_quote():
# 	# pick a random quote
# 	random_data = choice(all_quotes)
# 	quote = random_data['text']
# 	auth = random_data['author']
# 	bio = random_data['bio_link']

# 	# go to bio link of author
# 	# hint 1
# 	res_auth = requests.get(f"{BASE_URL}{bio}")
# 	soup_auth = BeautifulSoup(res_auth.text, "html.parser")
# 	auth_born_date = soup_auth.find(class_="author-born-date").get_text()
# 	auth_born_place = soup_auth.find(class_="author-born-location").get_text()
# 	hint1 = f"The author was born in {auth_born_date} {auth_born_place}"

# 	# hint 2 & hint 3
# 	hint2, hint3 = auth.split(" ")
# 	hint2 = f"The author's first name starts with {hint2[0]}"
# 	hint3 = f"The author's last name starts with {hint3[0]}"
# 	hints = [hint1, hint2, hint3]
# 	return (quote, auth, hints)


# play_again = 'y'
# while play_again == 'y':
# 	i = 0
# 	guesses_rem = 4
	
# 	quote, auth, hints = pick_a_quote()

# 	# ask a user about the author of the specified quote
# 	user_input = input(f"{quote}\n Who said this? Guesses remaining: {guesses_rem}. ")


# 	while guesses_rem != 0:
# 		if user_input.lower() != auth.lower():
# 			if guesses_rem > 1:
# 				hint = hints[i] 
# 				print(f"Here's a hint: {hint}") 
# 				guesses_rem -= 1
# 				user_input = input(f"Who said this? Guesses remaining: {guesses_rem}. ")
# 				i += 1
# 			else:
# 				print(f"Sorry, you've run out of guesses. The answer was {auth}")
# 				break
# 		else:
# 			print("You guessed it right! CONGRATULATIONS!!!")
# 			break
# 	play_again = input("Would you like to play again (y/n)? ")