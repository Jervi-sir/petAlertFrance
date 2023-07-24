import requests
import json
import pandas as pd
import time

# Start timer
start_time = time.time()

# Load your CSV file
df = pd.read_csv('contacts.csv')
print("csv loaded")  # Display the current index

# Limit to the first 50000 rows
df = df.iloc[100000:600000]

# Add a new column isDone
df['isDone'] = 0

# API information
url = "https://api.sendwithses.com/add-contact"
headers = {
    "Content-Type": "application/json",
    "template-key": "a2aa10aaoXDdbbbTsdtrFxT17Z3Ra7jqag8q5917P5g7Tj1aSYsg9MkXP2wG"
}

# Loop over rows in the dataframe
for index, row in df.iterrows():
    if index % 100 == 0:  # Check if index is a multiple of 100
        print(f"Processing index: {index}")  # Display the current index

    # Data to send with the POST request
    data = {
        "email": row['email'],  # Assuming the column in CSV is 'email'
        "country": row['country'],  # Replace with actual data
        "mobile": row['phone'],    # Replace with actual data
        "add_tags": "Petalert"
    }

    # Send the request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # If the request was successful, mark it as done
    if response.status_code == 200:
        df.loc[index, 'isDone'] = 1

    # Optional: sleep for a short time to prevent hitting API rate limits
# Save the updated dataframe to a new CSV file
df.to_csv('path_to_your_file_updated.csv', index=False)

# End timer
end_time = time.time()

# Calculate and print elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
