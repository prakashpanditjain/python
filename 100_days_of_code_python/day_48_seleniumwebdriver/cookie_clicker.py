import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the language selection element to be clickable
language = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN"))
)
language.click()

# Wait for the main game to load by waiting for the big cookie element to be present
cookie = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

# Wait a bit more to ensure the game is fully loaded
time.sleep(5)

# Click the cookie at a 0.001-second rate
while True:
    try:
        cookie.click()
    except StaleElementReferenceException:
        # Re-find the cookie element if it becomes stale
        cookie = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "bigCookie"))
        )
