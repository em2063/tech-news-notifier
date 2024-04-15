import requests
from bs4 import BeautifulSoup

url = "https://news.sky.com/technology" #get news website
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

TOKEN = "6959722588:AAE7Xeg4z48rIrHb1M4e5j4ubPs6QS0apFk" # API token to access Telegram
CHAT_ID = "6532403018" #ID to access chat with bot

def getHeadlines():
    articles = soup.select("section")[0]

    headlines = [a for a in articles.find_all('a')] # get headlines (a tags) from articles section
    headlines_text = [h.text for h in headlines] # get text version of article
    headlines_links = [a.get("href") for a in headlines] # find the link to every article
    headlines_urls = [f"http://news.sky.com/{l}" for l in headlines_links] # create functional url to webpage of article

    return headlines_text, headlines_urls #return info for headlines

def main():
    hText, hUrl = getHeadlines()
    for t, u in zip(hText, hUrl):
        message = f'{t}: {u}' #create message
        t_url =   f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}" #send message to telegram

if __name__ == "__main__":
    main()


