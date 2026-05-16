from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("http://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("packy")
#
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("packyrich")

first_name = driver.find_element(By.NAME, value="email")
first_name.send_keys("packy@email.com")

search = driver.find_element(By.CSS_SELECTOR, value=".btn-block")
search.click()

