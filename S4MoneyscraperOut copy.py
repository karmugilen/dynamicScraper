from autoscraper import AutoScraper
import json


url = 'https://www.amazon.in/Seiko-Analog-White-Dial-Watch-SUR312P1/dp/B084KP1GKP?ref_=ast_sto_dp'
# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.

scraper = AutoScraper()
scraper.load('pricelists')
#scraper.keep_rules(['rule_zy9f','rule_2oz5'])

result = scraper.get_result_similar(url,group_by_alias=True)

# print(result)

print(result[''][0])

url_price_data = {
    'url': url,
    'price': result[''][0] if result[''] else 'Not found'
}

# Convert the data to JSON format
json_data = json.dumps(url_price_data, indent=2)

# Write the JSON data to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)

print(f'Data written to output.json:\n{json_data}')