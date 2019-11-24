# Importing flat files from the web
# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
# print(df.head())

# Opening and reading flat files from the web
# We have just imported a file from the web, saved it locally and 
# loaded it into a DataFrame. If we just wanted to load a file from 
# the web into a DataFrame without first saving it locally, we can do 
# that easily using pandas. In particular, we can use the function 
# pd.read_csv() with the URL as the first argument and the separator 
# sep as the second argument.

# Import packages
# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')

# Print the head of the DataFrame
# print(df.head())


# Importing non-flat files from the web
# Import package
import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, sheet_name=None)

# Print the sheetnames to the shell
# print(xls.keys())	# odict_keys(['1700', '1900'])

# Print the head of the first sheet (using its name, NOT its index)
# print(xls['1700'].head())	



# We can send http request for the html page using urllib or requests package

# Performing HTTP requests in Python using urllib
# Get requests to extract info from teach page
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))	# <class 'http.client.HTTPResponse'>

# Extract the response: html
html = response.read()

# Print html
# print(html)

# Be polite and close the response!
response.close()

# Performing HTTP requests in Python using requests
# Import package
import requests

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)


# Beautiful Soup
# Parse and extract structurued data from HTML
# Make tag soup beautiful and extract information
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
# print(pretty_soup)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

# Print the title of Guido's webpage to the shell
# print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
# print(guido_text)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    # print(link['href'])
    print(link.get('href'))
