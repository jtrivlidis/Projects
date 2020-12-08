import requests

csv_url = 'https://assets.datacamp.com/production/repositories/287/datasets/5b1e4356f9fa5b5ce32e9bd2b75c777284819cca/gapminder.csv'
req = requests.get(csv_url)
url_content = req.content
csv_file = open('Gapminder.csv', 'wb')

csv_file.write(url_content)
csv_file.close()

# Dataset in use is the world bank estimates of population size between the year 1950 up to 2100
import requests
import pandas as pd
#import matplotlib.pyplot as plt

# Accessing dataset from the internet
csv_url = 'https://assets.datacamp.com/production/repositories/287/datasets/5b1e4356f9fa5b5ce32e9bd2b75c777284819cca/gapminder.csv'
req = requests.get(csv_url)
url_content = req.content

# create local csv file
csv_file = open('Gapminder.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

# creating a dataframe
df = pd.read_csv('./Gapminder.csv')
print(df)
col_year = df['year']

print(col_year)