import pandas as pd
import re

df_A = pd.read_csv('BO_Client_Person.csv')
df_B = pd.read_csv('export_All-Users_2023-07-18_07-55-06.csv')

# Convert to lower case and strip spaces
df_A['email'] = df_A['email'].str.lower().str.strip()
df_B['email'] = df_B['email'].str.lower().str.strip()

# Remove the emails from df_A that exist in df_B
df_A_filtered = df_A[~df_A['email'].isin(df_B['email'])].copy()

# Initialize a counter for emails ending with 'gmail' or 'gmail.com.com'
count_modified = [0]

# Define a function to adjust emails ending with 'gmail' or 'gmail.com.com', convert to lowercase, and count them
def adjust_email(email):
    if email.endswith('gmail'):
        count_modified[0] += 1
        return email + '.com'
    elif email.endswith('.com.com'):
        count_modified[0] += 1
        return email[:-4]  # Remove the extra '.com'
    elif email.endswith('.fr.com'):
        count_modified[0] += 1
        return email[:-4]  # Remove the extra '.fr'
    elif email.endswith('@sfr'):
        count_modified[0] += 1
        return email + '.fr'
    else:
        return email

df_A_filtered['email'] = df_A_filtered['email'].apply(adjust_email)

# Define a function to validate emails
def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if(re.search(regex,email)):  
        return True  
    else:  
        return False

# Apply the validate_email function and only keep valid emails
df_A_filtered = df_A_filtered[df_A_filtered['email'].apply(validate_email)].copy()

print(f"Number of emails modified: {count_modified[0]}")

df_A_filtered['role'] = 'User'

df_A_filtered.to_csv('B_filtered.csv', index=False)
