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


# functions to get souped courses content of a website and return faculty, course, level, award, duration
def get_course_divs(divs):
    faculty = []
    course = []
    level = []
    award = []
    duration = []
    for div in divs:
        faculty.append(div.find('div', class_="vacancy-head vacancy-head-default").text.replace("\n", '').replace("\t", '').strip()[11:])
        course.append(div.h5.text)
        level.append(div.find('div' ,class_="vacancy-details").text.split("\n")[2].split()[-1])
        award.append(div.find('div' ,class_="vacancy-details").text.split("\n")[3].split(":")[-1].strip().split("-")[0].strip())
        duration.append(int(div.find('div' ,class_="vacancy-details").text.split("\n")[3].split(":")[-1].split('-')[-1].strip().split()[0]))
        
    return faculty, course, level, award, duration



# function to get news page and return title, article_link
def get_page(page):
    base = 'http://www.mubas.ac.mw'
    title = []
    article_link = []
    
    divs = page.find_all('div', class_= 'col-sm-6 news-snippet')
    for div in divs:
        title.append(div.h4.text)
        article_link.append(f"{base}{div.a['href']}")
        
    
    return title, article_link



# functions to get the beautfied news content of a website and return article, date, author 
def get_souped_news(news):
    author = news.find('div', class_='news-content').text.replace('\n','').replace('\xa0','')
    date = news.find('div', {"class":"news-date"}).text.split("\t")[8].split('\n')[0].strip()
    article = news.find('div', {"class":"news-date"}).text.split("\t")[4].split('\xa0')[0].strip()
    
    return article, date, author 



# this is a dictionary for courses repositories
courses_dict = {
    'faculty':[],
    'course':[],
    'level':[],
    'award':[],
    'duration':[]
}

# this is a pandas  dataframe for all courses
def create_repo(faculty, course, level, award, duration):
    courses_dict['faculty'].extend(faculty)
    courses_dict['course'].extend(course)
    courses_dict['level'].extend(level)
    courses_dict['award'].extend(award)
    courses_dict['duration'].extend(duration)
    
    
    return pd.DataFrame(courses_dict)