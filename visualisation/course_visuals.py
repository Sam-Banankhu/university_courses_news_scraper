# importing necessary libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(11,7), dpi=100)
 
# adding root folder to the system path
sys.path.insert(0, '/home/pandas/Desktop/scraper/')

# reading the data
df = pd.read_csv('courses.csv')



plt.barh(df['faculty'].value_counts().keys(), df['faculty'].value_counts())
plt.title("GRAPH SHOWING FACULTIES AND THEIR PROGRAMS")
plt.ylabel('Faculties')
plt.xlabel('Number of programs')
plt.savefig('fig1.png')
plt.show()



sns.barplot(data = df, y = df['faculty'].value_counts().keys(), x = df['faculty'].value_counts())
plt.title("GRAPH SHOWING FACULTIES AND THEIR PROGRAMS")
plt.ylabel('Faculties')
plt.xlabel('Number of programs')
plt.savefig('fig2.png')
plt.show()
# print(df.head())

sns.barplot(data = df, x = 'faculty', y = 'duration', hue="level")
plt.title('GRAPHICS')
plt.ylabel('Faculties')
plt.xlabel('Number of programs')
plt.savefig('fig3.png')
plt.show()