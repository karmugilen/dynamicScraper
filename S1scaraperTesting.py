from autoscraper import AutoScraper

url = 'https://www.amazon.in/Seiko-SRPD63K1-SEIKO-Sports-Auto/dp/B07Y53F3L4/ref=sr_1_18?crid=FV2QNJQYWW33&keywords=automatic+watch&qid=1704822266&sprefix=automatic+watch%2Caps%2C234&sr=8-18'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["22,375"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)