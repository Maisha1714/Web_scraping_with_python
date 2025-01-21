from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
link_list = []

driver.get('https://www.daraz.com.bd/eyeshadow-palette?page=1')
driver.maximize_window()
total_pages = driver.find_element(By.CSS_SELECTOR, '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child(1) > div > div > div > div > ul > li.ant-pagination-total-text').text
for page_no in range(1, 3):
    driver.get(f'https://www.daraz.com.bd/eyeshadow-palette?page={page_no}')
   
    for i in range(1, 13):
        type_i = str(i)
        try:
    
            link = driver.find_element(
                By.CSS_SELECTOR,
                f'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child({type_i}) > div > div > div.buTCk > div.RfADt > a'
            ).get_attribute('href')
            link_list.append(link)
        except Exception as e:
            print(f"Error for item {i} on page {page_no}: {e}")

# Print the first link (example)
if link_list:
    print(link_list[0])
    driver.get(link_list[0])  # Navigate to the first link

time.sleep(10)
driver.quit()
