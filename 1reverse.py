import pandas as pd

# Load your CSV file
df = pd.read_csv('aggregation_query.csv')

# Sort by a column in descending order
# Replace 'column_to_sort' with the name of the column you want to sort by
df_reversed = df.iloc[::-1]

# If you want to save the reversed DataFrame to a new CSV file:
df_reversed.to_csv('reversedfile.csv', index=False)
