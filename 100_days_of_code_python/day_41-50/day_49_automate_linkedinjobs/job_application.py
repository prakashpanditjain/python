from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

# Setup WebDriver
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

# LinkedIn Credentials from Environment Variables
linkedin_username = os.environ.get('LINKEDIN_USERNAME')
linkedin_password = os.environ.get('LINKEDIN_PASSWORD')

# Open LinkedIn Job Search URL
url = "https://www.linkedin.com/jobs/search/?currentJobId=4181266293&distance=25&f_AL=true&f_WT=2&geoId=92000000&keywords=Data%20Engineer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true"
driver.get(url)
print("Opened LinkedIn job portal")

time.sleep(2)
# Wait for Sign-in button
try:
    sign_in = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="base-contextual-sign-in-modal"]//button'))
    )
    sign_in.click()
    print("Clicked the sign-in button")
except TimeoutException:
    print("Sign-in button not found")

time.sleep(5)
# Wait for username & password fields
try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "session_key"))
    )
    username.send_keys(linkedin_username)
    print("Username entered")

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "session_password"))
    )
    password.send_keys(linkedin_password)
    print("Password entered")

    # Click Sign-in button
    sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    sign_in_button.click()
    print("Signed in successfully")

except ElementNotInteractableException:
    print("Login fields not found")


#site is not responding properly I will continue this later