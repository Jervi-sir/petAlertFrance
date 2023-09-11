import pandas as pd

# Load CSV file into Pandas DataFrame
df = pd.read_csv('aggregation_query.csv') 

# Reverse order of rows 
df = df.iloc[::-1]

# Write reversed DataFrame back to a new CSV file
reversed_csv = 'reversed_data.csv'
df.to_csv(reversed_csv, index=False)