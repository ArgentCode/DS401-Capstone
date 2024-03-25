## https://www.youtube.com/watch?v=SPM1tm2ZdK4&t=855s
## https://www.youtube.com/watch?v=USrjHgO9Niw python selenium button clicking

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
import re

college_file_list = ['ames, ia', 'college station, tx', 'minneapolis, mn'] #### Need to make sure they are in "City, St" format
# with open('Collegetowns2.csv', 'r') as file:
#     # Create a CSV reader object using DictReader
#     for line in file:
#         city = line[:-1].replace(',', '-').replace(' ', '-')
#         college_file_list.append(city)

options=Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                            options=options)

grocery_dict =	{
  "Dark Red Kidney Beans": "https://www.target.com/p/bush-39-s-dark-red-kidney-beans-16oz/-/A-13593955#lnk",
  "Ground Beef": "https://www.target.com/p/all-natural-85-15-ground-beef-1lb-good-38-gather-8482/-/A-13288295#lnk=sametab",
  "year": 1964
}

for item in grocery_dict: 
    for college in college_file_list:

        # Dark red kidney beans ames iowa
        driver.get("")

        # Find the element by data-test attribute
        price_element = driver.find_element(By.CSS_SELECTOR, '[data-test="product-price"]')
        print(price_element.text)

        time.sleep(3)

        # Find the button by its ID
        webStoreButton = driver.find_element(By.ID, "web-store-id-msg-btn")

        # Click the button
        webStoreButton.click()
        time.sleep(2)

        inputBox = driver.find_element(By.ID, "zip-or-city-state")
        inputBox.send_keys(college) # Need to input "city, st"

        lookupButton =  driver.find_element(By.CSS_SELECTOR, '[data-test="@web/StoreLocationSearch/button"]')
        lookupButton.click()
        time.sleep(2)

        ShopStoreButton =  driver.find_element(By.CSS_SELECTOR, '[data-test="@web/StoreMenu/ShopThisStoreButton"]')
        ShopStoreButton.click()

        time.sleep(3)
        # ID of the button id="zip-code-id-btn"


driver.close()
