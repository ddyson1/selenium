from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options, executable_path="/Users/devindyson/Desktop/chromedriver")

url = "http://www.google.com"

driver.get(url)

element = driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
element.send_keys("Massachusetts Institute of Technology")

element.send_keys(Keys.ENTER)

element = driver.find_element_by_css_selector("#rso > div:nth-child(1) > div > div > div > div.yuRUbf > a > h3").click()

print(driver.current_url)

time.sleep(5)

driver.close()
