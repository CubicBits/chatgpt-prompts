import requests
import csv
import json

# Download CSV file
url = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv"
response = requests.get(url)
data = response.content.decode('utf-8')

# Convert CSV to JSON
csv_reader = csv.DictReader(data.splitlines())
json_data = json.dumps([row for row in csv_reader])

# Write JSON to file
with open('prompts.json', 'w') as f:
    f.write(json_data)