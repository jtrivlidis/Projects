import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

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
print(df.head())
gdp_cap = df['gdp_cap']
life_exp = df['life_exp']
pop = df['population']

# Building a scatter plot to visualize world development data

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# Store pop as a numpy array:
np_pop = np.array(df['population'])
print(np_pop)

# Scale population
np_pop = np_pop * 0.0000025

#Set the colour values
col = ['r', 'g', 'b', 'b', 'y', 'k', 'g', 'r', 'r', 'g', 'b', 'y', 'g', 'b', 'y', 'g', 'b', 'b', 'r', 'b', 'y', 'b', 'b', 'y', 'r', 'y', 'b', 'b', 'b', 'y', 'b', 'g', 'y', 'g', 'g', 'b', 'y', 'y', 'b', 'y', 'b', 'b', 'b', 'g', 'g', 'b', 'b', 'g', 'b', 'g', 'y', 'b', 'b', 'y', 'y', 'r', 'g', 'g', 'r', 'r', 'r', 'r', 'g', 'r', 'g', 'y', 'r', 'r', 'b', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'r', 'b', 'b', 'b', 'y', 'r', 'g', 'b', 'b', 'r', 'b', 'r', 'g', 'k', 'y', 'b', 'b', 'g', 'r', 'r', 'y', 'y', 'y', 'r', 'g', 'g', 'y', 'b', 'g', 'b', 'b', 'r', 'b', 'g', 'b', 'r', 'g', 'g', 'b', 'b', 'g', 'r', 'b', 'b', 'g', 'g', 'r', 'r', 'b', 'r', 'b', 'y', 'b', 'g', 'b', 'g', 'y', 'y', 'y', 'r', 'r', 'r', 'b', 'b']

# Specify c and alpha inside plt.scatter()
plt.scatter(x=gdp_cap, y=life_exp, s=np_pop, c=col, alpha=0.8)

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
plt.grid(True)

# Display the plot
plt.show()