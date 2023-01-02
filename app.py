# importing neccesary library
import pandas as pd
import numbers as np
from bs4 import BeautifulSoup
import requests
from time import sleep


# functions to get the link of a website and return souped content
def get_link(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'html.parser')
    
    return soup


# functions to get the beautfied content of a website and return divs containers for courses
def get_souped_courses(soup):
    results = soup.find('div', class_ = 'row vacancy-container')
    divs = results.find_all('div', {'class':'col-sm-6'})
    
    return divs


# functions to get the beautfied news content of a website and return article, date, author 
def get_souped_news(news):
    author = news.find('div', class_='news-content').text.replace('\n','').replace('\xa0','')
    date = news.find('div', {"class":"news-date"}).text.split("\t")[8].split('\n')[0].strip()
    article = news.find('div', {"class":"news-date"}).text.split("\t")[4].split('\xa0')[0].strip()
    
    return article, date, author 