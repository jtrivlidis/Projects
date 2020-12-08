import pandas as pd
import requests
# Accessing dataset from the internet
csv_url = 'https://assets.datacamp.com/production/repositories/5386/datasets/1a0ab2e8557930ec06473c16521874e516a216ae/homelessness.csv'
req = requests.get(csv_url)
url_content = req.content

# create local csv file
csv_file = open('Homelessness.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

# Creating a dataframe
homelessness = pd.read_csv('./Homelessness.csv')
print(homelessness.head())

# Inspect parts of the dataframe
print(homelessness.values)
print(homelessness.columns)
print(homelessness.index)

# Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())

# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]

# See the result
print(ind_gt_10k)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]

# See the result
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)

# Adding new columns
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]
homelessness["p_individuals"] = homelessness["individuals"]/homelessness["total"]

# See the result
print(homelessness)

# Which state has the highest number of homeless individuals per 10,000 people in the state?
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)
