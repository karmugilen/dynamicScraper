from autoscraper import AutoScraper

url = 'https://www.amazon.in/Seiko-Analog-White-Dial-Watch-SUR312P1/dp/B084KP1GKP?ref_=ast_sto_dp'

# Define the expected data points you want to extract
wanted_list = ["$249.00", "Seiko Men's SUR312P1 Watch", "4.5 out of 5 stars", "10"]

# Create a new scraper and provide the URL
scraper = AutoScraper()
scraper.build(url, wanted_list)

# Get the updated rules
rules = scraper.get_rules()

# Print the updated rules
for rule in rules:
    print(rule)

# Save the updated rules
scraper.save('pricelists')
