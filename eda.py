import pandas as pd

#loading the dataset
df = pd.read_csv('news.csv')

# print(df.head())

date_mod = pd.to_datetime(df['date'])
date_mod = date_mod.dt.strftime('%d-%m-%Y')

# inserting a column with the date dtype
df.insert(0, column = 'date_mod', value = date_mod)
# print(date_mod)
# droping the date column
df.drop(columns = 'date', inplace =True)


df.sort_values(by='date_mod', ascending=True, inplace=True, ignore_index= True)

df.rename(columns={'date_mod':'date', 'article': 'author', 'author':'article' }, inplace=True)
print(df.head())