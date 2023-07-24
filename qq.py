import pandas as pd
import json

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

# Read the csv file
df = pd.read_csv('your_file.csv')

# Function to format the 'address.city' cell content
def format_content(row):
    city = row['address.city']
    country = row['country']
    state = row['state']
    if is_json(city):
        return city
    else:
        return json.dumps({'nom': city, 'country': country, 'state': state})

# Apply the function to the dataframe
df['address.city'] = df.apply(format_content, axis=1)

# Save the dataframe back to csv
df.to_csv('your_filsse.csv', index=False)