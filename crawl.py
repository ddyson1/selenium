from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1420x780")

driver = webdriver.Chrome(options=chrome_options, executable_path="/Users/devindyson/Desktop/scripts/chromedriver")

url = "https://news.ycombinator.com/"

driver.get(url)
time.sleep(2)

#by css
elements = driver.find_elements_by_css_selector(".storylink")
storyTitles = [el.text for el in elements]
storyUrls = [el.get_attribute("href") for el in elements]

elements = driver.find_elements_by_css_selector(".score")
scores = [el.text for el in elements]

elements = driver.find_elements_by_css_selector(".sitebit a")
sites = [el.get_attribute("href") for el in elements]
