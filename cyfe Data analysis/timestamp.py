import pandas as pd
from datetime import datetime

def convert_milliseconds_to_datetime(x):
    try:
        # Try to convert assuming it's a Unix timestamp in milliseconds
        return pd.to_datetime(int(x), unit='ms').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        # If conversion fails, return the original string
        return x

# Read the CSV file into a DataFrame
df = pd.read_csv("alert.csv")

# Transform the specific columns

df['dateCreated'] = df['dateCreated'].apply(convert_milliseconds_to_datetime)
df['date'] = df['date'].apply(convert_milliseconds_to_datetime)
df['datePublished'] = df['datePublished'].apply(convert_milliseconds_to_datetime)
df['boostDate'] = df['boostDate'].apply(convert_milliseconds_to_datetime)
df['payment_date'] = df['payment_date'].apply(convert_milliseconds_to_datetime)
df['shareDate'] = df['shareDate'].apply(convert_milliseconds_to_datetime)
df['plannedDate'] = df['plannedDate'].apply(convert_milliseconds_to_datetime)


# Save the updated DataFrame back to a new CSV file
df.to_csv("your_updated_file.csv", index=False)
