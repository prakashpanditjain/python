from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(articles.text)


search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)