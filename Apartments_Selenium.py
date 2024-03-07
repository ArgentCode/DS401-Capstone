## https://www.youtube.com/watch?v=SPM1tm2ZdK4&t=855s

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import pandas as pd

college_file_list = ['ames-ia', 'college-station-tx', 'minneapolis-mn']
# college_file_list = []/
    
    # Use the pattern to match and filter characters
    

# with open('Collegetowns2.csv', 'r') as file:
#     # Create a CSV reader object using DictReader
#     for line in file:
#         city = line[:-1].replace(',', '-').replace(' ', '-')
#         college_file_list.append(city)

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
    time.sleep(2)
    # filename = city + "-html.txt"
    # with open(filename, 'w') as file:
    #     file.write(html.encode('utf-8').decode('ascii', 'ignore'))
    # file.close()
    ## Insert some gabe code here! 
    i= i+1
    if i > 3:
        break

driver.close()