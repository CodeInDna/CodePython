import sqlite3
import requests
from bs4 import BeautifulSoup

# url of book store
url = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"


def scrape_books(url):
	# Request url
	response = requests.get(url)

	# Intialize BS
	soup = BeautifulSoup(response.text, "html.parser")
	books = soup.find_all("article")	
	
	all_books = []
	for book in books:
		book_data = get_title(book),get_price(book),get_rating(book)
		all_books.append(book_data)
	print(all_books)
	

def get_title(book):
	return book.find("h3").find("a")["title"]

def get_price(book):
	price = book.select(".price_color")[0].get_text()
	return float(price.replace("£","").replace("Â", ""))

def get_rating(book):
	ratings = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
	rating_para = book.select(".star-rating")[0]
	rating_word = rating_para.get_attribute_list("class")[-1]
	return ratings[rating_word]

scrape_books(url)
# Extract Data we want
# Save data to database 