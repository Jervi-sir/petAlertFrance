import pandas as pd

df = pd.read_csv('sanitized_no_duplicates.csv')

last_100_rows = df.tail(1000)

last_100_rows.to_csv('last_1k_rows.csv', index=False)