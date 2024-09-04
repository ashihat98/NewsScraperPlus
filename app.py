from flask import Flask, request, render_template, send_file
import os
import pandas as pd
from scraper import scrape_news
from data_processor import process_data
from database import save_to_database  # Optional, only if you want to save to a database
import openpyxl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        #Scrape the data
        news_data = scrape_news(url)

        if news_data:
            #Process the data
            processed_data = process_data(news_data)

            #Save to an Excel file
            excel_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'news.xlsx')
            processed_data.to_excel(excel_path, index=False)

            # In case i want in athe future to save to a database 
            # save_to_database process

            #Send the Excel file to the user
            return send_file(excel_path, as_attachment=True)
        else:
            return "No data scraped. Please check the URL."
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
