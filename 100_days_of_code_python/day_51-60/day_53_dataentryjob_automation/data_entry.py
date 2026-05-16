import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())

all_link_tags = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link['href'] for link in all_link_tags]

all_addresses_tag = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [addresses.getText().replace(" | "," ").strip() for addresses in all_addresses_tag]


all_price_element = soup.select(".PropertyCardWrapper span")
all_prices = [all_prices.getText().replace("/mo","").split("+")[0] for all_prices in all_price_element]


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfjcaYrgk3ZC1t3G-QfYQ1W0spXuGmrxdW0LUOPLSiDRm0hqw/viewform?usp=header")

for n in range(len(all_links)):
    link = all_links[n]
    address = all_addresses[n]
    price = all_prices[n]


    time.sleep(5)
    try:
        address_ans = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        address_ans.send_keys(f"{address}")

        price_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        price_text.send_keys(f"{price}")


        link_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        link_text.send_keys(f"{link}")


        submit_button = driver.find_element(By.CSS_SELECTOR, value=".l4V7wb.Fxmcue span")
        print("Submit button found")
        submit_button.click()
        print("Clicked submit button")

        time.sleep(5)

        another_response_tab = driver.find_element(By.LINK_TEXT, value="Submit another response")
        print("Submit another response link found")
        another_response_tab.click()
        print("Submit another response clicked")

        time.sleep(5)

    except Exception as e:
        print(f"Error is : {e}")



