from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = [
    "amara raja",
    "Natco Pharma",
    "Kalyan Jewellers"   
]


driver = webdriver.Chrome()


# Set the download folder path

download_folder = r"D:\02code\01python\dynamicScraper"

# Create ChromeOptions object
chrome_options = webdriver.ChromeOptions()

# Set the download directory preference
prefs = {"download.default_directory": download_folder}
chrome_options.add_experimental_option("prefs", prefs)

# Create a WebDriver instance with the specified options
driver = webdriver.Chrome(options=chrome_options)

def test_one_components():
    driver.get("https://trends.google.com/trends/explore?q=itc&date=now%201-d&geo=IN&hl=en")


def test_two_components(url):
    driver.get("https://trends.google.com/trends/explore?date=now%207-d&geo=IN&q="+url+"&hl=en")
    #driver.get("https://trends.google.com/trends/explore?date=now%207-d&q="+url+"&hl=en")
    time.sleep(1)

    driver.implicitly_wait(164)
    time.sleep(1)

    submit_button = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]/i")
    submit_button.click()
    #driver.quit()



def test_one_two_combain(url):
    test_one_components()
    for i in url:
        test_two_components(i)

test_one_two_combain(url)
