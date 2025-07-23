import requests
from bs4 import BeautifulSoup

def scrape_metadata(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.title.string if soup.title else "No Title"
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return title, text
