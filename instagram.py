from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from decouple import config
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options, executable_path="/Users/devindyson/Desktop/chromedriver")

url = "https://instagram.com"
user = config('IGUSER')
passphrase = config('IGPASS')

driver.get(url)
time.sleep(1)

elements = driver.find_elements_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
username = elements[0]
username.clear()
username.send_keys(user)

elements = driver.find_elements_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")
username = elements[0]
username.clear()
username.send_keys(passphrase)

elements = driver.find_elements_by_css_selector("#loginForm > div > div:nth-child(3)")
submit = elements[0]
submit.click()

time.sleep(5)

driver.close()
