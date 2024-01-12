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

print(result)
