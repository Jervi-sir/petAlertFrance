import pandas as pd

df = pd.read_csv('sanitized_no_duplicates.csv', nrows=0)

column_names = df.columns.tolist()

for column_name in column_names:
    print(column_name)
