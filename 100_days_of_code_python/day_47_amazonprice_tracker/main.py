import os

from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://appbrewery.github.io/instant_pot/"
myemail= "my_email@gmail.com"
mypassword = os.environ.get("SMTPLIB")

if not mypassword:
    print("SMTPLIB is not set !!")

response = requests.get(url)

# 1. Scrape the website to get the price of items
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

#  2. Get the price of the item
price_tag = soup.find_all(name="span", class_= "aok-offscreen")
title_tag = soup.find_all(name="span", id="productTitle")

price_tag = price_tag[0].getText().split("$")[1]
title_tag = title_tag[0].getText()[:50].strip()
# .split(",")[0]

print(title_tag)

print(price_tag)

target_price = 100

# 3. Send an email if the price of the item is less than the target price
if float(price_tag) < target_price:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=myemail, password=mypassword)
        print("Login Successful")

        connection.sendmail(
            from_addr=myemail,
            to_addrs="email_to_send@gmail.com",
            msg=f"Subject:Amazon Price Alert\n\nThe price of \n{title_tag} is less than {target_price}\n{url}"
        )
        print("Mail Sent")