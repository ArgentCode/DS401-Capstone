## https://www.youtube.com/watch?v=SPM1tm2ZdK4&t=855s

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import pandas as pd

college_file_list = ['ames-ia', 'college-station-tx']
# college_file_list = []
    
    # Use the pattern to match and filter characters
    

with open('Collegetowns2.csv', 'r') as file:
    # Create a CSV reader object using DictReader
    for line in file:
        city = line[:-1].replace(',', '-').replace(' ', '-')
        college_file_list.append(city)

options=Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options )

i = 1
print("Firing up for loop")
for city in college_file_list:
    url = "https://www.apartments.com/" + city + "/max-1-bedrooms/"
    print(url)
    driver.get(url)

    html = driver.page_source
    prices = PriceExtraction(html)
    time.sleep(2)
    # filename = city + "-html.txt"
    # with open(filename, 'w') as file:
    #     file.write(html.encode('utf-8').decode('ascii', 'ignore'))
    # file.close()
    ## Insert some gabe code here! 
    i= i+1
    time.sleep(3)
    if i > 1:
        break

driver.close()

def PriceExtraction(html):

    # Remove tabs and newlines
    pricing = re.sub("[\t|\n]+", "", html)

    # # Extract all matches
    matches = re.findall(r'aria-label="[\\w\\s[:punct:]]*>[^<]*<p class="property-pricing">[^<]*</p>', pricing)

    # # Filter out None values and convert to DataFrame
    pricing_df = pd.DataFrame([x for x in matches if x is not None], columns=['Text'])

    # # Separate AptName and Price
    # pricing_df[['AptName', 'Price']] = pricing_df['Text'].str.extract(r'aria-label="([^"]*)">[^<]*<p class="property-pricing">([^<]*)</p>')

    # # Clean AptName and Price columns
    # pricing_df['AptName'] = pricing_df['AptName'].str.replace('aria-label="', '').str.replace(',.*$', '')
    # pricing_df['Price'] = pricing_df['Price'].str.replace('class="property-pricing">\\$', '').str.replace('</p>', '')

    # # Separate Price into Price1 and Price2
    # pricing_df[['Price1', 'Price2']] = pricing_df['Price'].str.split(' - ', expand=True)

    # # Drop the original Text and Price columns
    # pricing_df.drop(columns=['Text', 'Price'], inplace=True)
    print(pricing_df)
    return pricing_df