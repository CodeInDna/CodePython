# import necessary modules
import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

# define the url's
BASE_URL = "http://quotes.toscrape.com/"

def scrape_quotes():
	# define a data strcuture to store the details
	all_quotes = []
	url = "/page/1"
	# visit each page
	while url:
		# get html
		response = requests.get(f"{BASE_URL}{url}")
		soup = BeautifulSoup(response.text, "html.parser")

		# scrap the necessary things out of html
		quotes_divs = soup.select(".quote")		# gives a list of all divs with class name "quote"
		# scrap the quote(text), author's name and bio-link out of divs
		for quote in quotes_divs:
			text = quote.find(class_="text").get_text()
			author = quote.find(class_="author").get_text()
			bio_link = quote.find("a")['href']
			all_quotes.append(
				{
					"text" : text,
					"author": author,
					"bio_link": bio_link
				}
			)

		# search next button
		next_btn = soup.find(class_="next")
		# if next btn is present, then get the url
		url = next_btn.find("a")["href"] if next_btn else None
	sleep(1)
	return all_quotes
# print(all_quotes)


# write quotes to a csv file
def write_quotes(quotes):
	with open("quotes.csv","w") as file:
		headers = ["text","author","bio_link"]
		csv_writer = DictWriter(file, fieldnames= headers)
		csv_writer.writeheader()
		for quote in quotes:
			csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)
