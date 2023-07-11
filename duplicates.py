import pandas as pd

# Load your CSV file
df = pd.read_csv('alert_june.csv')
total_count = len(df)

# Define the columns that you want to check for duplicates
duplicate_columns = ['animal.0.photo']

# Detect duplicates
duplicates = df.duplicated(subset=duplicate_columns, keep=False)

# Get only the duplicate rows
duplicate_rows = df[duplicates]


duplicate_count = len(duplicate_rows)

print('total nb rows = ' , total_count)
print('total duplicates = ' , duplicate_count)