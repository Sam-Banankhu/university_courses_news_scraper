# importing neccesary library
import pandas as pd
import numbers as np
from bs4 import BeautifulSoup
import requests
from time import sleep

def get_link(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'html.parser')
    
    return soup