import pandas as pd
import requests
# Accessing dataset from the internet
csv_url = 'https://assets.datacamp.com/production/repositories/463/datasets/82e9842c09ad135584521e293091c2327251121d/tweets.csv'
req = requests.get(csv_url)
url_content = req.content

# create local csv file
csv_file = open('Tweets.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

# Creating a dataframe
tweets = pd.read_csv('./Tweets.csv')
print(tweets.head())

# Defining functions to build a dictionary of languages based on twitter data

def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    langs_count = {}
    col = tweets[col_name]

    for entry in col:

        if entry in langs_count.keys():
            langs_count[entry] += 1
        else:
            langs_count[entry] = 1

    return langs_count

result = count_entries(tweets, 'lang')

print(result)

# Defining functions with multiple arguments
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    cols_count = {}

    for col_name in args:

        col = tweets[col_name]

        for entry in col:

            if entry in cols_count.keys():
                cols_count[entry] += 1

            else:
                cols_count[entry] = 1

    return cols_count


result1 = count_entries(tweets, 'lang')
result2 = count_entries(tweets, 'lang', 'source')

print(result1)
print(result2)

# Selecting retweets using lambda functions

result = filter(lambda x: x[0:2]=='RT', tweets['text'])
res_list = list(result)

for tweet in res_list:
    print(tweet)

# Raising value errors within functions

def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    cols_count = {}
    col = tweets[col_name]

    for entry in col:

        # Extract column from DataFrame: col
        col = tweets[col_name]

        # Iterate over the column in DataFrame
        for entry in col:

            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1

            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

result1 = count_entries(tweets, col_name = 'lang')

print(result1)