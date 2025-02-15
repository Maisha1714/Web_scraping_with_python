import selenium as se
import webdriver_manager as wm
import selenium.webdriver as sw
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t
import random
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--incognito')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
)

# Launch Chrome
driver = uc.Chrome(options=chrome_options)

driver.get('https://www.google.com/')
t.sleep(random.uniform(3, 6))  

driver.refresh()

search_box = driver.find_element(By.NAME, 'q')
query = "Laptop shop Near Mirpur"
for char in query:
    search_box.send_keys(char)
    t.sleep(random.uniform(0.1, 0.3))  # Human-like typing delay

search_box.send_keys(Keys.RETURN)
t.sleep(random.uniform(5, 10))

try:
    re_captcha = driver.find_element(By.CLASS_NAME, 'g-recaptcha')
    print("⚠️ CAPTCHA detected! Please solve it manually.")
    t.sleep(20)  # Wait for user to solve CAPTCHA
except NoSuchElementException:
    print("✅ No CAPTCHA detected.")
driver.refresh()

map = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[1]/div/div/div/a[1]').click()

height = driver.execute_script('return document.body.scrollHeight')
print(height)


scrollable_div = driver.find_element(By.CLASS_NAME, "m6QErb")  # Container class

for _ in range(34):  # Adjust the range for more scrolling
    ActionChains(driver).move_to_element(scrollable_div).send_keys(Keys.PAGE_DOWN).perform()
    t.sleep(2)  # Wait for new results to load

shops = driver.find_elements(By.CLASS_NAME, "qBF1Pd")
phones = driver.find_elements(By.CLASS_NAME, "UsdlK")

dict = {}
for i in range(len(phones)):

    dict[shops[i].text]=phones[i].text

print(dict)

t.sleep(100)
#python contact_of_laptop_shop.py
