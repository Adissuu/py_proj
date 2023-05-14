import requests
from bs4 import BeautifulSoup
import smtplib


my_email = "pythonanglecode@gmail.com"
password = "hvcppnquacdpfmbe"

object="https://www.amazon.ca/Sony-WH-1000XM5-" \
       "Cancelling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_2?crid=1JEL90IDYYP74&keywords=sony%2Bwh-" \
       "1000xm5&qid=1684027995&sprefix=sony%2Caps%2C121&sr=8-2&th=1"

price_target = 400

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0 (Edition std-1)",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=object, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

price_dollars = soup.find('span', class_="a-price-whole").getText()
price_cents = soup.find('span', class_="a-price-fraction").getText()
total_price = float(f"{price_dollars.split('.')[0]}.{price_cents.split('.')[0]}")
print(total_price < price_target)

if total_price < price_target:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs="duboisg35610@gmail.com", msg=f"Subject:Sony WH-1000XM5"
                                                                                       f"\n\nSheeeeeeeeeeeeesh! The Sony headphones from {object} are currently at {price_dollars}{price_cents}!")