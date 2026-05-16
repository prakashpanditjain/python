from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://www.python.org")

event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(event_names)):
    pass
    events[n+1] = {
        "time": event_time[n].text,
        "names" : event_names[n].text,
    }

print(events)

driver.quit()
