## https://www.youtube.com/watch?v=SPM1tm2ZdK4&t=855s

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import re

# college_file_list = []
# with open('Collegetowns2.csv', 'r') as file:
#     # Create a CSV reader object using DictReader
#     for line in file:
#         city = line[:-1].replace(',', '-').replace(' ', '-')
#         college_file_list.append(city)

options=Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options )


driver.get("https://www.target.com/p/bush-39-s-dark-red-kidney-beans-16oz/-/A-13593955#lnk")

# Dark red kidney beans ames iowa
# https://www.target.com/p/bush-39-s-dark-red-kidney-beans-16oz/-/A-13593955#lnk
html = driver.page_source
time.sleep(5)


driver.close()
