from bs4 import BeautifulSoup
import requests
import smtplib
import os
from  dotenv import load_dotenv

load_dotenv()

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
TARGET_PRICE = 200


SMTP_PORT = os.environ["SMTP_PORT"]
SMTP_GMAIL_SERVER = os.environ["SMTP_GMAIL_SERVER"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
RECEIPT_EMAIL = os.environ["RECEIPT_EMAIL"]


response = requests.get(URL, 
                        headers= {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36", 
                                  "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
                                  "x-https": "on",
                                  "upgrade-insecure-requests" : "1"
                                  }
                                )
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="a-offscreen")
product_title = soup.find(name="span", id="productTitle").getText().strip()
product_links = soup.find_all(name="link")

price_without_currency = (float(price.getText().split("$")[1]))

for link in product_links:
    if link.get("rel")[0] == "canonical":
        product_link = link.get("href")

if price_without_currency < TARGET_PRICE:
    with smtplib.SMTP(SMTP_GMAIL_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIPT_EMAIL,
            msg=f"Subject: Lowest Prices👆\n\n \
                Product: {product_title}\n \
                Price: {price_without_currency}\n \
                Link: {product_link}".encode('utf-8'))