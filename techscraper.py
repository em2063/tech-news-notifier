import requests
from bs4 import BeautifulSoup

url = "https://news.sky.com/technology" #get news website

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
articles = soup.select("section")[0]

headlines = [a for a in articles.find_all('a')] # get headlines from articles section
headlines_text = [h.text for h in headlines] # get text version of article
headlines_links = [a.get("href") for a in headlines] # find the link to every article
headlines_urls = [f"http://news.sky.com/{l}" for l in headlines_links] # create functional url to webpage of article

print(headlines_urls)

