from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from decouple import config
import time

# PROXY = "99.99.99.99:1111" # IP:PORT or HOST:PORT

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
# prefs={"profile.managed_default_content_settings.images": 2, "disk-cache-size": 4096}
# chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=chrome_options, executable_path="/Users/devindyson/Desktop/scripts/chromedriver")
# driver.get("http://whatismyipaddress.com")

url = "https://twitter.com/login"
user = config('TWITTERUSER')
passphrase = config('TWITTERPASS')

driver.get(url)
time.sleep(1)

elements = driver.find_elements_by_css_selector(".r-fdjqy7")
username = elements[0]
username.clear()
username.send_keys(user)

elements = driver.find_elements_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-iphfwy.r-s1qlax.r-ttdzmv > div > input")
password = elements[0]
password.send_keys(passphrase)

elements = driver.find_elements_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(8) > div")
submit = elements[0]
submit.click()

time.sleep(5)

driver.close()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

"""
#find all the links
links = driver.find_elements_by_partial_link_text('')
#get the first one
l = links[0]
#click on it
driver.execute_script("arguments[0].click();", l)
"""
