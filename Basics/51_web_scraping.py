#-----------Web Scraping------------#
# What is Scraping
# Web Scraping involves programmatically grabbing data from a web page
# Three steps: Download, extract data, do something with data

# Why Scrape?
# There's data on a site that you want to store or analyze
# You can't get by other means (e.g. API)
# You want to pragrammatically grab the data(instead of manual copying/pasting)

# Is it ok to scrape?
# Some websites don't want people scraping them
# Best practice: consult the robots.txt file
# If making many requests, time them out
# If you're too aggresive, your IP can be blocked

# Beautiful Soup(bs4) Package
# To extract data from HTML, we'll use Beautiful Soup
# Install it with pip
# Beautiful Soup lets us navigate through HTML with Python
# Beautiful Soup doesn't download HTML - for this, we need the requests module!
html = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>First HTML page</title>
</head>
<body>
	<div id="first">
		<h3 data-example="yes">hi</h3>
		<p>more text.</p>
	</div>
	<ol>
		<li class="special">This list item is also special.</li>
		<li class="special super">This list item is special.</li>
		<li>This list item is not special.</li>
	</ol>
	<div>bye</div>
</body>
</html>
"""

from bs4 import BeautifulSoup
# Accessing Tags
# parsing and navigating HTML
soup = BeautifulSoup(html, "html.parser")
print(soup.body)
print('*********************')

print(soup.body.div)
print('*********************')

print(soup.find('div'))
print('*********************')

print(soup.find_all('div'))			# gives a list with 2 divs
print('*********************')	

print(soup.find(id="first"))
print('*********************')

print(soup.find_all(class_="special"))	# [<li class="special">This list item is special.</li>, <li class="special">This list item is also special.</li>]
print('*********************')

print(soup.find_all(attrs={"data-example":"yes"}))	# [<h3 data-example="yes">hi</h3>]
print('*********************')

# Select using CSS Selectors(always gives a list)
print(soup.select("#first"))	# [<div id="first"><h3 data-example="yes">hi</h3><p>more text.</p></div>]
print(soup.select("#first")[0])	# <div id="first"><h3 data-example="yes">hi</h3><p>more text.</p></div>
print('*********************')

print(soup.select(".special"))	# [<li class="special">This list item is special.</li>, <li class="special">This list item is also special.</li>]
print('*********************')

print(soup.select("[data-example]"))	# [<h3 data-example="yes">hi</h3>]
print('*********************')

print(soup.select("[data-example=yes]"))	# [<h3 data-example="yes">hi</h3>]
print('*********************')

# Accessing Data in Elements
# get_text : access the inner text in an element
# name : tag_name
# attrs : dictionary of attributes
# You can also acces attribute values using brackets
el = soup.select(".special")[0]

#get_text
print(el.get_text())		# This list item is special.
print('*********************')

all_el = soup.select(".special")
for el in all_el:
	print(el.get_text())
# This list item is special.
# This list item is also special.
print('*********************')

#name
print(el.name)		# li
print('*********************')

#attrs
print(el.attrs)		# {'class': ['special']}
print('*********************')

print(el.attrs['class'])		# ['special']}
print('*********************')

#brackets
print(soup.find("div")["id"])	# first
print('*********************')

# Navigating Via Tags
	# parent/ parents
	# contents
	# next_sibing / next_sibings
	# previous_sibling / previous_siblings

# Navigating Via Searching
	# find_parent/ find_parents
	# find_next_sibing / find_next_sibings
	# find_previous_sibling / find_previous_siblings


# Via Tags***********************************************************************************
# contents (consider new line as well '\n')
data = soup.body.contents
print(data)		# gives a comma seperated list along with '\n' and contents within a body tag 
# ['\n', <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>, '\n', <ol>
# ...so on]
print('*********************')

data2 = soup.body.contents[1].contents
print(data2)	#['\n', <h3 data-example="yes">hi</h3>, '\n', <p>more text.</p>, '\n']
print('*********************')

# next_sibling
data3 = soup.body.contents[1].next_sibling
print(data3)		# gives nothing becoz next sibling of div is '\n'
print('*********************')

# next_sibling
data4 = soup.body.contents[1].next_sibling.next_sibling
print(data4)
#<ol>
# <li class="special super">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>
print('*********************')

# previous_sibling
data5 = soup.find(class_="super").previous_sibling.previous_sibling
print(data5)	# <li class="special">This list item is also special.</li>
print('*********************')

# parent
data6 = soup.find(class_="super").parent
print(data6)	# <li class="special">This list item is also special.</li>
#<ol>
# <li class="special">This list item is also special.</li>
# <li class="special super">This list item is special.</li>
# <li>This list item is not special.</li>
# </ol>
print('*********************')


# Via Searching***********************************************************************************
# find_next_sibling
data7 = soup.find(id="first").find_next_sibling()
print(data7)
# <ol>
# <li class="special">This list item is also special.</li>
# <li class="special super">This list item is special.</li>
# <li>This list item is not special.</li>
# </ol>		
print('*********************')

# # next_sibling
data8 = soup.body.find(id="first").find_next_sibling().find_next_sibling()
print(data8) 	# <li class="special">This list item is also special.</li>
print('*********************')

# previous_sibling
data9 = soup.find(class_= "super").parent()
# [<li class="special">This list item is also special.</li>, <li class="special super">This list item is special.</li>, <li>This list item is not special.</li>]
print(data9)
# print('*********************')
