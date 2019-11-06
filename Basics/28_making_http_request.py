#------------making http request using python-------------#
#Using the requests module

import requests
response = requests.get("https://news.ycombinator.com/")
print(response)		#<Response [200]>
print(response.status_code)		#200
# print(response.ok)	#True
# print(response.headers)	#prints all the metdata
# print(response.text)	#prints all the data(text) with html


response1 = requests.get("https://news.ycombinator.com/sfafaf") 
print(response1)		#<Response [404]>
print(response1.status_code)		#404


url = "https://icanhazdadjoke.com/"
# res = requests.get(url, headers={'Accept':'text/plain'})
res = requests.get(url, headers={'Accept':'application/json'})
print(res.text)	#type is str
data = res.json()	#type is python dictionary
print(data["joke"])	#The joke