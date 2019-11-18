#-----------Web Scraping Program------------#
import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(["title","link","date"])

	for article in articles:
		a_tag = article.find("a")
		url = a_tag["href"]
		title = a_tag.get_text()
		datetime = article.find("time")["datetime"]
		csv_writer.writerow([title,url,datetime])