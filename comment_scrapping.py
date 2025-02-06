#importing necessary libraries
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Base URL for the product reviews
base_url = 'https://www.daraz.com.bd/products/18-i335584256-s1632145286.html?'

# Open the webpage
driver.get(base_url)
time.sleep(2)  # Allow the page to load

# Scroll to load initial comments
height = driver.execute_script("return document.body.scrollHeight")
for i in range(0, height+2000, 30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.7)

# Custom pagination pattern for 5 pages
values = []
for i in range(1, 6):  # Scraping only 5 pages
    if i >= 4 and i < 5:
        values.append(4)
    elif i == 5:
        values.append(5)
    else:
        values.append(i)

# Scrape comments from multiple pages
all_comments = []

for page in values:
    try:
        # Find all comment elements
        comments = driver.find_elements(By.CLASS_NAME, 'content')

        for comment in comments:
            text = comment.text.strip()  #strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
            if text:
                all_comments.append(text)

        print(f"Scraped {len(comments)} comments from page {page}")

        # Find and click the next page button (modify selector if needed)
        next_button = driver.find_element(By.XPATH, f'//button[contains(text(), "{page}")]')
        driver.execute_script("arguments[0].click();", next_button)

        time.sleep(3)  # Wait for the next page to load

    except Exception as e:
        print(f"Error on page {page}: {e}")
        break

# Print all scraped comments
print("\n--- Collected Comments ---\n")
for comment in all_comments:
    print(comment)

# Close the driver
driver.quit()
