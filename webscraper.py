from bs4 import BeautifulSoup
import requests

url = 'https://twitter.com/naveenbandarage'

response = requests.get(url, timeout=5)

content = BeatifulSoup(response.content, "html.parser")

print(content)

#From here I am going to add more code

#unsure if tweet container actually exists. ANd have doubts on accessiation of certain areas need to have a further play around. 
#Might have to use API. 

for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):  
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text.encode('utf-8'),
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text.encode('utf-8'),
        "tweet": tweet.find('p', attrs={"class": "content"}).text.encode('utf-8'),
        "likes": tweet.find('p', attrs={"class": "likes"}).text.encode('utf-8'),
        "shares": tweet.find('p', attrs={"class": "shares"}).text.encode('utf-8')
    }
    print tweetObject


print("This is the webscraper.py file")

