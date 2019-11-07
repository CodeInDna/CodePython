#------------API Exercise--------------#
from pyfiglet import figlet_format
from requests import get
from random import choice
import autopep8

# Heading of an Exercise
print(figlet_format("Dad Joke 3000"))

# Ask for user input
topic = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"

# get response from api
response = get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
).json()

# get total no of jokes
no_of_jokes = response['total_jokes']

# get all the jokes
res = response["results"]

if no_of_jokes > 1:
    print(f"I found {no_of_jokes} jokes about {topic}. Here's one: ")
    print(choice(res)["joke"])
elif no_of_jokes == 1:
    print(f"I found one joke about {topic}. Here's one: ")
    print(res[0]['joke'])
else:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again.")
