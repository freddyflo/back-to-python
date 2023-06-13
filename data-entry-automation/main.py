from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests
import time
service = Service("/Users/aklamanu/Documents/tut/python/py-bootcamp/chromedriver")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A37.888501634392355%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.661908651347005%2C%22west%22%3A-122.63417331103516%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A593661%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%2C%22mapZoom%22%3A12%7D"


response = requests.get(ZILLOW_URL, 
                        headers= 
                                {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36", 
                                  "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
                                  "x-https": "on",
                                  "upgrade-insecure-requests" : "1"
                                  })

soup = BeautifulSoup(response.text, "html.parser")
# price_card = soup.select("ul li div span")
price_cards = soup.find_all(name="span", class_="srp__sc-16e8gqd-1 jLQjry")


appt_info = soup.find_all(name="div", class_="StyledPropertyCardDataWrapper-c11n-8-85-1__sc-1omp4c3-0 jVBMsP property-card-data")

appt_addresses = [ appt_address.find(name="address").getText() for appt_address in appt_info ]

appt_prices = [ appt_price.find(name="span").getText().split()[0].split("+")[0].split("/mo")[0] for appt_price in appt_info]

appt_links = soup.find_all(name="div", class_="StyledPropertyCardPhoto-c11n-8-85-1__sc-ormo34-0 hMbZrX srp__sc-1gxvsd7-0 gJxiTi")

appt_pages = [appt_link.find(name="img").get("src") for appt_link in appt_links]

# Form filling 
FORM_URL = "https://forms.gle/YNRkYEBRH2yuN6jd8"
driver.get(FORM_URL)

print(len(appt_addresses))

for n in range(len(appt_addresses)):
  driver.get(FORM_URL)
  time.sleep(3)
  address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
  address_input.send_keys(appt_addresses[n])

  price_per_month = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
  price_per_month.send_keys(appt_prices[n])

  property_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
  property_link.send_keys(appt_pages[n])

  submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
  submit_btn.click()

driver.quit()
