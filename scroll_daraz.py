from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get('https://www.daraz.com.bd/products/18-i335584256-s1632145286.html?')
height = driver.execute_script("return document.body.scrollHeight")
print(f'Scroll_Height is',height)

for i in range(0,height+2000,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

all_comments = driver.find_elements(By.CLASS_NAME,'content')

for i in all_comments:
    print(i.text)


time.sleep(45)