from autoscraper import AutoScraper
import json

url = 'https://www.amazon.in/MARVIK-Bluetooth-SmartWatch-Activity-Functionality/dp/B0B5V8MBMC/ref=sr_1_5?keywords=watch&qid=1704994917&sr=8-5'

scraper = AutoScraper()
scraper.load('pricelists')

result = scraper.get_result_exact(url, grouped=True)

# Remove the currency symbol from the result
result_no_currency = {url: [price.replace('\u20b9', '') for price in value] for key, value in result.items()}

# Load existing data from the JSON file
try:
    with open('output.json', 'r') as json_file:
        existing_data = json.load(json_file)
except FileNotFoundError:
    existing_data = {}

# Append or update the data with the new result
existing_data.update(result_no_currency)

# Write the updated data back to the JSON file
with open('output.json', 'w') as json_file:
    json.dump(existing_data, json_file, indent=2)

print("Data appended to output.json")


