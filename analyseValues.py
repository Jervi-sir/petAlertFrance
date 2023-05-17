import pandas as pd

df = pd.read_csv('aggregation_query.csv')

for col in df.columns:
    print(f"---> {col} :")
    #print(df[col].value_counts().idxmax())
    print(df[col].unique())

