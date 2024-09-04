import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = soup.find_all('a')
    news_list = []

    for article in articles:
        title = article.text.strip()
        link = article['href']
        if not link.startswith('http'):
            link = url + link

        # Filtering articles based on URL path and excluding non-news sections
        if '/news/articles/' in link and not any(keyword in title.lower() for keyword in ['home', 'sport', 'travel', 'weather']):
            news_data = {'title': title, 'link': link}
            news_list.append(news_data)


    return news_list
