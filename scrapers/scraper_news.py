# importing necessary libraries
import pandas as pd
import sys
from time import sleep
 
# adding root folder to the system path
sys.path.insert(0, '/home/pandas/Desktop/scraper/')
import app


base = 'http://www.mubas.ac.mw'
for i in range(41):
    articles = []
    dates = []
    authors = []
    
    page_link =f"{base}/news?page={i+1}"
    
    page = app.get_link(page_link)
    title, article_link = app.get_page(page)
    
    for link in article_link:
        news = app.get_link(link)
        article, date, author = app.get_souped_news(news)
        articles.append(article)
        dates.append(date)
        authors.append(author)
    
    df_news = create_news_repo(title, articles, dates, authors, article_link)
    sleep(.2)