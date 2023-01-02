# importing necessary libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(11,7), dpi=100)
 
# adding root folder to the system path
sys.path.insert(0, '/home/pandas/Desktop/scraper/')

df = pd.read_csv('news_cleaned.csv')

# print(df.head())

# ploting authors and contributors against the number of news articles
sns.barplot(y = df['author'].value_counts().index, x = df['author'].value_counts(),)
plt.title("GRAPH SHOWING AUTHORS AND THEIR WORK")
plt.xlabel('Number of articles')
# plt.ylabel('Authors')
plt.savefig('fig3.png')
plt.show()