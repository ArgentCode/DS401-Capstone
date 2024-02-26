## https://www.youtube.com/watch?v=SPM1tm2ZdK4&t=855s

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options=Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options )

driver.get("https://www.apartments.com/ames-ia/2-bedrooms/")
driver.maximize_window()

# links=driver.find_elements("xpath", "//a[@href]")
# for link in links:
#     if "Books" in link.get_attribute("innerHTML"):
#         link.click()
#         break

# book_links = driver.find_elements("xpath",
#                                   "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 in 1')]]]")

html = driver.page_source
file = open("htmltext.txt", "w", encoding="utf-8")
file.write(html)
file.close()
print(html)

driver.close()