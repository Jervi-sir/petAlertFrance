import pandas as pd

input_file = 'alert_to_upload_27July_02_august.csv'
output_file = 'alert_to_upload_27July_02_august_added_onecsv'

df = pd.read_csv(input_file)

df['id'] = df['id'] + 1

df.to_csv(output_file, index=False)

print("IDs incremented and saved to", output_file)
