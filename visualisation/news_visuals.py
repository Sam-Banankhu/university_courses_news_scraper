# importing necessary libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figsize'] = (16, 9)
 
# adding root folder to the system path
sys.path.insert(0, '/home/pandas/Desktop/scraper/')

df = pd.read_csv('news_cleaned.csv')

print(df.head())