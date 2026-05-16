import os

from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://www.amazon.in/gp/product/B07NBCP3S5/ref=ox_sc_act_image_3?smid=A2AL6IVND0I91F&th=1"
myemail= "my_email@gmail.com"
mypassword = os.environ.get("SMTPLIB")

if not mypassword:
    print("SMTPLIB is not set !!")

response = requests.get(url)

# 1. Scrape the website to get the price of items
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

#  2. Get the price of the item
price_tag = soup.find_all(name="span", class_= "a-price-whole")
title_tag = soup.find_all(name="span", id="productTitle")

price_tag = price_tag[0].getText()
title_tag = title_tag[0].getText().strip()
# .split(",")[0]

print(title_tag)

print(price_tag)

target_price = 100

# 3. Send an email if the price of the item is less than the target price
# if float(price_tag) < target_price:
#     with smtplib.SMTP("smtp.gmail.com",587) as connection:
#         connection.starttls()
#         connection.login(user=myemail, password=mypassword)
#         print("Login Successful")
#
#         connection.sendmail(
#             from_addr=myemail,
#             to_addrs="email_to_send@gmail.com",
#             msg=f"Subject:Amazon Price Alert\n\nThe price of \n{title_tag} is less than {target_price}\n{url}"
#         )
#         print("Mail Sent")