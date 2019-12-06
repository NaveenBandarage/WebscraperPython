from bs4 import BeautifulSoup
import requests

url = 'https://twitter.com/naveenbandarage'

response = requests.get(url, timeout=5)

content = BeatifulSoup(response.content, "html.parser")

print(content)

print("This is the webscraper.py file")

