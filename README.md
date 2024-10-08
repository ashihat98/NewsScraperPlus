NewsScraperPlus
NewsScraperPlus is a Python-based web application that allows users to scrape news articles from any provided news website URL. 
The application processes the scraped data, cleans it, and generates a downloadable Excel file containing the titles and links of the articles.

Features
Web Scraping: Scrape news articles from any URL.
Data Processing: Clean and process the scraped data for consistency.
Excel Export: Export the data to an Excel file for easy download.
Optional Database Storage: Save the data to an SQLite database (if needed).
User-Friendly Interface: Simple and intuitive web interface built with Flask.
Technologies Used
Python: The core programming language used for the application.
Flask: Web framework used to build the web interface.
BeautifulSoup: Library used for web scraping.
Pandas: Data analysis library used for processing and exporting data.
SQLite: Optional database storage.
                                                                
Installation:
To run this project locally, follow these steps:


git clone https://github.com/ashihat98/NewsScraperPlus.git
cd NewsScraperPlus/src

python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

pip3 install -r requirements.txt

pip3 install flask pandas sqlalchemy beautifulsoup4 requests openpyxl

python3 app.py
