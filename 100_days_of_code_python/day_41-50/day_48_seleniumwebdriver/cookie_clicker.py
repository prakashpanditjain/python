import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://orteil.dashnet.org/cookieclicker/")
input_keys = "Mi4wNTJ8fDE3NDIxMzIxMjMzNDI7MTc0MjEzMjEyMzM0MjsxNzQyMjAwMDAwNDQzO1NjaWVuY2UgU3BhY2VzaGlwO2pvaXFjOzAsMSwwLDAsMCwwLDB8MTExMTExMDExMDAxMDExMDAxMDEwMTEwMDAxfDM1NjM0MTU3OTUuNDgzMTAyOzM2Nzg3MzY2Mzg3LjQzNDMyNjs0MTYxOzE3OzEzOTIwMDQxOS44MTY4OTQzNTs1NzswOzA7MDswOzA7MDswOzA7MDsxNzswOzA7MDswOzA7MDs7MDswOzA7MDswOzA7MDstMTstMTstMTstMTstMTswOzA7MDswOzc1OzA7MDswOzA7MTc0MjE3Nzc4NDU3OTswOzA7OzQxOzA7MDs0MzM1NDkxLjkwNzkwMTcyODs1MDswOzA7fDEwOSwxMDksMTczOTg3NTIxNywwLCwwLDEwOTs4NCw4NCw2NTU5OTEwMzYsMCwsMCw4NDs2OCw2OCw0MDUxNjIwMzAsMCwsMCw2ODs1NSw1NSwxMjAzNjkzMDUwLDAsLDAsNTU7NDQsNTUsMjc2ODE5NzQxMSwwLCwwLDQ0OzM2LDM2LDgzNjQwNzkzNDMsMCwsMCwzNjsyMiwyMywxMTk2MTQ2MTUwMSwwLCwwLDIyOzEwLDEwLDY5MDcxMTEyNTMsMCwsMCwxMDsyLDIsMTMxNjYxMjMwMCwwLCwwLDI7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDt8MTExMTExMTExMTExMDAxMTExMTExMTExMTExMTExMTExMTExMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTEwMTExMTExMTExMTExMTExMDEwMTAwMDExMTEwMDExMDAwMDAwMDAxMTAwMDAxMDEwMTExMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMDAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTEwMDAwMDAxMTExMDAwMDAwMDAxMTEwMDAwMDAwMDAxMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMHwxMTExMTEwMDAwMDAwMDAwMTExMTExMDAwMDAwMDAxMTEwMTExMTAwMTEwMTEwMTAwMTEwMTAwMDAwMDAwMDAwMDAwMTEwMDAxMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDEwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwfHw%3D%21END%21"
main_window = driver.current_window_handle

# Wait for the language selection element to be clickable
language = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN"))
)
language.click()

# Wait for the main game to load by waiting for the big cookie element to be present
cookie = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

def click_option_button():
    while True:
        try:
            option_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="prefsButton"]/div'))
            )
            option_button.click()
            print('clicking option button')
            time.sleep(5) # Wait for the options menu to load
            import_save_button = driver.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[4]/a[2]')
            import_save_button.click()

            time.sleep(5) # Wait for the import save menu to load
            for handle in driver.window_handles:
                if handle != main_window:
                    driver.switch_to.window(handle)
                    break
            text_area = driver.find_element(By.XPATH, value='//*[@id="textareaPrompt"]')
            text_area.send_keys(input_keys, Keys.ENTER)
            
            
            #close option window
            for handle in driver.window_handles:
                if handle == main_window:
                    driver.switch_to.window(main_window)
                    break
            time.sleep(5)
            option_close_button = driver.find_element(By.XPATH, value='//*[@id="menu"]/div[1]')
            option_close_button.click()
            print('closing option window')
            break
        except StaleElementReferenceException as e:
            print(f"printing exception {e}")
            continue

click_option_button()


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
