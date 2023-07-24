import pandas as pd

# Read in the CSV file
df = pd.read_csv('latest_sanitized_all.csv')

# Get the number of filled rows for each column
num_filled_rows = df.count()

# Set pandas options to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Print the number of filled rows for each column
print(num_filled_rows)