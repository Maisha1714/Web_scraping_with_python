import time
import random
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# ✅ Fix SSL Certificate Issues for macOS
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# ✅ Use Safari or Chrome (Mac Compatibility)
USE_SAFARI = False  # Change to True if you want to use Safari instead of Chrome

if USE_SAFARI:
    driver = webdriver.Safari()
else:
    # ✅ Start Undetected Chrome WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # Bypass detection
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
    
    driver = uc.Chrome(options=chrome_options)

# ✅ Open Google
driver.get('https://www.google.com/')
time.sleep(random.uniform(3, 6))  # Random delay

# ✅ Refresh the page
driver.refresh()

# ✅ Find search box and enter query with human-like typing
search_box = driver.find_element(By.NAME, 'q')
query = "Laptopshop Near Mirpur"
for char in query:
    search_box.send_keys(char)
    time.sleep(random.uniform(0.1, 0.3))  # Human-like typing delay

search_box.send_keys(Keys.RETURN)
time.sleep(random.uniform(5, 10))  # Let results load

# ✅ Handle Google reCAPTCHA manually (if detected)
try:
    re_captcha = driver.find_element(By.CLASS_NAME, 'g-recaptcha')
    print("⚠️ CAPTCHA detected! Please solve it manually.")
    time.sleep(20)  # Wait for user to solve CAPTCHA
except NoSuchElementException:
    print("✅ No CAPTCHA detected.")

# ✅ Try Clicking Google Maps Link
try:
    map_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Maps")
    map_button.click()
    time.sleep(5)
except NoSuchElementException:
    print("❌ Could not find the Maps button.")

# ✅ Scroll Down (Human-like Behavior)
height = driver.execute_script('return document.body.scrollHeight')
print("Page Height:", height)

try:
    scrollable_div = driver.find_element(By.CLASS_NAME, "m6QErb")  # Google Maps container

    for _ in range(10):  # Scroll multiple times
        ActionChains(driver).move_to_element(scrollable_div).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(random.uniform(2, 4))  # Random delay
except NoSuchElementException:
    print("❌ Could not find scrollable div.")

# ✅ Extract Shop Names & Phone Numbers
shop_data = {}
try:
    shops = driver.find_elements(By.CLASS_NAME, "qBF1Pd")
    phones = driver.find_elements(By.CLASS_NAME, "UsdlK")

    for i in range(min(len(shops), len(phones))):
        shop_data[shops[i].text] = phones[i].text

    print("✅ Shop Data:", shop_data)
except NoSuchElementException:
    print("❌ Could not extract shop details.")

# ✅ Wait before quitting
time.sleep(10)

# ✅ Quit Driver
driver.quit()
