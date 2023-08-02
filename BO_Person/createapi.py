import csv
import requests

# URL for the POST request
url = 'https://petalertglobal.com/version-test/api/1.1/wf/create-users-from-xano'
#url = 'https://petalertglobal.com/api/1.1/wf/create-users-from-xano'

# Headers for the POST request
headers = {
    'Authorization': 'Bearer 24a54af4a159afa7b706ccfa05cbaaac'
}

with open('B_filtered.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row['email']
        data = {'email': email}
        response = requests.post(url, headers=headers, data=data)
        
        # Print status and returned data for debugging
        print(response.status_code)
        print(response.json())
