import requests
from bs4 import BeautifulSoup

print("Begin operations!")

# Replace 'your_url' with the actual URL you want to scrape
url = 'https://www.walmart.com/ip/Great-Value-Dark-Red-Kidney-Beans-15-5-oz/10534045?athbdg=L1100&from=/search'
# Send an HTTP GET request to the URL
response = requests.get(url)


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the entire HTML content and print it
    html_content = soup.prettify()
    print(html_content)

else:
    print("Failed to retrieve the page. Status code:", response.status_code)