from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get('https://www.daraz.com.bd/products/18-i335584256-s1632145286.html?')
product_name = driver.find_element(By.XPATH,'//*[@id="module_product_title_1"]/div/div/h1').text
print(f'Product Name is : ',product_name)
time.sleep(0.5)

# Get the image element
image_element = driver.find_element(By.XPATH, '//*[@id="module_item_gallery_1"]/div/div[1]/div/img')  # Modify as needed

# Get the image URL
image_url = image_element.get_attribute("src")

# Download the image
image_data = requests.get(image_url).content

# Save the image
image_path = "downloaded_image.jpg"
with open(image_path, "wb") as file:
    file.write(image_data)

print(f"Image downloaded successfully as {image_path}")

product_price = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span').text
#//*[@id="module_product_price_1"]/div/div/span
print(f'Product Price is : ',product_price)

total_question_answered = driver.find_element(By.XPATH,'//*[@id="module_product_review_star_1"]/div/a[2]').text
print(f'Total Question Answered is : ',total_question_answered)

name_of_the_brand = driver.find_element(By.XPATH,'//*[@id="module_product_brand_1"]/div/a[1]').text
print(f'Name of the Brand is : ',name_of_the_brand)


height = driver.execute_script("return document.body.scrollHeight")
print(f'Scroll_Height is',height)

for i in range(0,height+2000,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.6)

product_details  = driver.find_element(By.XPATH,'//*[@id="module_product_detail"]/div/div/div[1]/div[1]/ul/li').text
print(f'Product Details is : ',product_details)
all_comments = driver.find_elements(By.CLASS_NAME,'content')

for i in all_comments:
    print(i.text)

time.sleep(50)

time.sleep(10000)

#//*[@id="module_item_gallery_1"]/div/div[1]/div/img
