import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd

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

        if '/news' in link:  # Filter for links containing "/news"
            news_data = {'title': title, 'link': link}
            news_list.append(news_data)

    return news_list

def save_to_excel(news_list, excel_path='news.xlsx'):
    df = pd.DataFrame(news_list)
    df.to_excel(excel_path, index=False)
    print(f"Data successfully saved to {excel_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py <url>")
        return

    url = sys.argv[1]
    news_data = scrape_news(url)
    if news_data:
        save_to_excel(news_data)
    else:
        print("No data scraped. Please check the URL.")

if __name__ == "__main__":
    main()
