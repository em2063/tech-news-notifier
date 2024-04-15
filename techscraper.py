import requests
from bs4 import BeautifulSoup

url = "https://news.sky.com/technology" #get news website

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

def getHeadlines():
    articles = soup.select("section")[0]

    headlines = [a for a in articles.find_all('a')] # get headlines (a tags) from articles section
    headlines_text = [h.text for h in headlines] # get text version of article
    headlines_links = [a.get("href") for a in headlines] # find the link to every article
    headlines_urls = [f"http://news.sky.com/{l}" for l in headlines_links] # create functional url to webpage of article

    return headlines_text, headlines_urls

def main():
    hText, hUrl = getHeadlines()
    headlines = set()
    for t, u in zip(hText, hUrl):
        if t not in headlines:
            print([t, u])
            headlines.add(t)


if __name__ == "__main__":
    main()


