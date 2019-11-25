# API: Application Programming Interface
# Protocols and routines
	# Building and interacting with software applications
# Bunch of Code that allows two software programs to communicate with each other
# Example if we want to stream twitter data by writting some code using python (language)
# then we use twitter api

# JSONs: JavaScript Object Notation
# Real-time serve to browser communication
# Douglas Crockford
# Human Readable

# Loading and exploring a JSON
import json

# Load json: json_data
with open('dataset/a_movie.json') as json_file:
	json_data = json.load(json_file)

# print key-value pair in json_data
# for key in json_data.keys():
	# print(key+ " : ", json_data[key])
	


# API requests
# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(type(r.text))	# str

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
# for k in json_data.keys():
    # print(k + ': ', json_data[k])	# print data as key-value pa


# API Authentication
# Working iwth twitter API
# You first need to have account, then go to twitter dashboard>create app
# > fill in some details
# The package tweepy is great at handling all the Twitter API OAuth 
# Authentication details for you. All you need to do is pass it your 
# authentication credentials. 
# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables
# access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
# access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
# consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
# consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# Streaming tweets
# Now that you have set up your authentication credentials, it is time 
# to stream some tweets!
# Initialize Stream listener
l = MyStreamListener()

# Create your Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(['clinton','trump','sanders','cruz'])

# Load and explore your Twitter data
# Now that you've got your Twitter data sitting locally in a text file, it's time to explore it!
# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

# Twitter data to DataFrame
# Now you have the Twitter data in a list of dictionaries, tweets_data, 
# where each dictionary corresponds to a single tweet. Next, you're 
# going to extract the text and language of each tweet. The text in a 
# tweet, t1, is stored as the value t1['text']; similarly, the language 
# is stored in t1['lang']
# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang'])

# Print head of DataFrame
print(df.head())

# A little bit of Twitter text analysis
# Now that you have your DataFrame of tweets set up, you're going to 
# do a bit of text analysis to count how many tweets contain the words 
# 'clinton', 'trump', 'sanders' and 'cruz'
import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False
# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])


# Plotting your Twitter data
# Import packages
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot the bar chart
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
