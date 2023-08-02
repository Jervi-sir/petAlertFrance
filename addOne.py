import pandas as pd

input_file = 'July15ToJuly30.csv'
output_file = 'July15ToJuly30_1.csv'

df = pd.read_csv(input_file)

df['id'] = df['id'] + 1

df.to_csv(output_file, index=False)

print("IDs incremented and saved to", output_file)
