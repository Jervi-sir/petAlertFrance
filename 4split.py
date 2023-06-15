import pandas as pd

df = pd.read_csv('z_splet_original_18.csv')


rows_per_file = 50000
num_files = -(-len(df) // rows_per_file)  # Ceiling division


for i in range(num_files):
    start = i * rows_per_file
    end = (i + 1) * rows_per_file
    df_part = df[start:end]
    df_part.to_csv(f'z_splet_original_18{i+1}.csv', index=False)
