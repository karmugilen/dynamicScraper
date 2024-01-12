from autoscraper import AutoScraper

url = 'https://www.amazon.in/Seiko-Analog-White-Dial-Watch-SUR312P1/dp/B084KP1GKP?ref_=ast_sto_dp'
# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.

scraper = AutoScraper()
scraper.load('pricelists')

#see the rule for filtering 
#result = scraper.get_result_exact(url, grouped=True) 

#using the rules for geting the info
scraper.keep_rules(['rule_jt7u','rule_l1u5'])


result = scraper.get_result_similar(url,group_by_alias=False)

# print(result)

print(result)

