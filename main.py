import requests
from bs4 import BeautifulSoup
from pprint import pprint


KEYWORDS = ['Дизайн', 'Фото', 'web', 'python']
HOST = 'https://habr.com/ru/'
URL = 'https://habr.com/ru/all/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('article', class_='tm-articles-list__item')
    articles = []
    for item in items:
        teg = item.find('div', class_='tm-article-snippet__hubs').find('span',class_='tm-article-snippet__hubs-item').find('a', class_='tm-article-snippet__hubs-item-link').find('span').get_text('span')
        for i in KEYWORDS:
            if teg == i:
                articles.append(
                    {
                        'teg' : item.find('div', class_='tm-article-snippet__hubs').find('span', class_='tm-article-snippet__hubs-item').find('a', class_='tm-article-snippet__hubs-item-link').find('span').get_text('span'),
                        'data': item.find('div', class_='tm-article-snippet__meta').find('span', class_='tm-article-snippet__datetime-published').find('time').get('title'),
                        'title': item.find('div', class_='tm-article-snippet').find('h2').find('a').get_text('span'),
                        'link' : HOST + item.find('div', class_='tm-article-snippet').find('h2').find('a').get('href'),
                    }
                )
        return articles

html = get_html(URL)
pprint(get_content(html.text))
