import csv
import json
import requests

# Initialize the writer for the new CSV file
with open('new_file.csv', 'w', newline='') as new_csvfile:
    fieldnames = ['id', 'animal_photo', 'variants', 'response']
    new_csvwriter = csv.DictWriter(new_csvfile, fieldnames=fieldnames)
    new_csvwriter.writeheader()

    # Read the original CSV file
    with open('imgs.csv', 'r') as old_csvfile:
        csvreader = csv.reader(old_csvfile)
        header = next(csvreader)  # Skip header row

        for row in csvreader:
            id = row[0]
            animal_photo = row[1]
            
            if not animal_photo:
                new_csvwriter.writerow({
                    'id': id,
                    'animal_photo': 'NULL',
                    'variants': 'No image',
                    'response': 'No image',
                    
                })
                continue

            try:
                image_names = json.loads(animal_photo)
            except json.JSONDecodeError:
                print(f"Could not decode JSON for ID: {id}")
                continue
            
            new_image_links = []
            variants_list = []
            for image_name in image_names:
                image_url = f"https://images.petalertfrance.com/images/{image_name}"
                url = "https://api.cloudflare.com/client/v4/accounts/51882c5879501e354d029f06c0bbd9a5/images/v1"

                headers = {
                    "Authorization": "Bearer 3NSyh1PGwJSYOsnGfQT501o6lGC6dZ7OEvsUahiz",  # Add your Bearer token here
                }

                data = {
                    "url": ("", image_url),
                    "metadata": ("", json.dumps({"key": "value", "id": id})),
                    "requireSignedURLs": ("", "false"),
                }

                response = requests.post(url, headers=headers, files=data)
                response_json = response.json()

                if 'result' in response_json and 'variants' in response_json['result']:
                    new_image_links.append(response_json['result']['variants'][0])
                    variants_list.extend(response_json['result']['variants'])

            # Writing the new URLs into a single animal_photo cell as an array
            new_csvwriter.writerow({
                'id': id,
                'animal_photo': json.dumps(new_image_links),
                'variants': json.dumps(variants_list),
                'response': json.dumps(response_json),

            })

            print(f"ID: {id}, New Image Links: {new_image_links}, Status: {response.status_code}, Response: {response.json()}")
