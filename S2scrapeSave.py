from autoscraper import AutoScraper

url = 'https://www.amazon.in/Seiko-Analog-White-Dial-Watch-SUR312P1/dp/B084KP1GKP?ref_=ast_sto_dp'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["₹20,586"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
# print(result)
for i in result:
    print(i)
scraper.save('pricelists')
