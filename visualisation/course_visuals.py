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

print(df.head())
