from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link_dict = {} 

driver.get('https://www.daraz.com.bd/eyeshadow-palette?page=1')
driver.maximize_window()

try:
    total_items = driver.find_element(
        By.CSS_SELECTOR,
        '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div.xYcXp > div > div.Ck3Nt > div > div > span:nth-child(1)'
    ).text
    print(f"Total items: {total_items}")
    print(type(total_items))
except Exception as e:
    print(f"Error fetching total items: {e}")

for page_no in range(1, 3): 
    driver.get(f'https://www.daraz.com.bd/eyeshadow-palette?page={page_no}')
    product_links = []  
    for i in range(1, 13): 
        try:
            link = driver.find_element(
                By.CSS_SELECTOR,
                f'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child({i}) > div > div > div.buTCk > div.RfADt > a'
            ).get_attribute('href')
            product_links.append(link)
        except Exception as e:
            print(f"Error for item {i} on page {page_no}: {e}")

    link_dict[page_no] = product_links
if link_dict:
    print("Links by page:")
    for page, links in link_dict.items():
        print(f"Page {page}: {len(links)} products")
        print(links)
time.sleep(10000)
