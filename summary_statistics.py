import pandas as pd
import numpy as np
import requests
# Accessing dataset from the internet
csv_url = 'https://assets.datacamp.com/production/repositories/5386/datasets/5110afec30fc30bc5f3cf67b188d1513c3d6d940/sales_subset.csv'
req = requests.get(csv_url)
url_content = req.content

# create local csv file
csv_file = open('Walmart_sales.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

# Creating a dataframe
sales = pd.read_csv('./Walmart_sales.csv')
print(sales.head())

# Mean and median
print(sales.info())
print(sales["weekly_sales"].mean())
print(sales["weekly_sales"].median())

# Summarizing dates
print(sales["date"].max())
print(sales["date"].min())

# Efficient summaries
def iqr(column):
### A custom IQR function
    return column.quantile(0.75) - column.quantile(0.25)

print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

# What percent of sales occurred at each store type?
sales_all = sales["weekly_sales"].sum()
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(f"Proportion by store type A, B, and C {sales_propn_by_type}")

# Calculations with .groupby()
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# Multiple grouped summaries
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

print(sales_stats)
print(unemp_fuel_stats)

# Pivoting on one variable
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

print(mean_sales_by_type)
print(mean_med_sales_by_type)
print(mean_sales_by_type_holiday)

