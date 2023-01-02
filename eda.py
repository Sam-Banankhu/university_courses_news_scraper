import pandas as pd

df = pd.read_csv('news.csv')

# print(df.head())

date_mod = pd.to_datetime(df['date'])
date_mod = date_mod.dt.strftime('%d-%m-%Y')


df.insert(0, column = 'date_mod', value = date_mod)
# print(date_mod)