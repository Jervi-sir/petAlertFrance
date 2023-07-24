import pandas as pd
import re

# Function to check if email is valid
def check_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, str(email)):
        return True
    return False

# Read CSV
df = pd.read_csv('latest_sanitized_all.csv')

# Drop duplicates
df = df.drop_duplicates(subset=['email', 'phone number', 'country'])

# Select only desired columns
df = df[['email', 'phone number', 'country']]

# Remove rows with empty emails
df = df.dropna(subset=['email'])

# Remove rows with invalid emails
df = df[df['email'].apply(check_valid_email)]

# Write to new CSV
df.to_csv('output.csv', index=False)
