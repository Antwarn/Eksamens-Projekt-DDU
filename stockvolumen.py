import requests
from bs4 import BeautifulSoup

# Replace 'url' with the URL you want to scrape
url = 'https://www.investing.com/equities/microsoft-corp'

# Send a request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the same class name
    elements = soup.find_all(class_='key-info_dd-numeric__ZQFIs')

    # Check if there are any elements with the class name
    if elements:
        # Get the first element that matches the class name
        target_element = elements[9]

        # Print the content of the desired element
        print(target_element.get_text())

    else:
        print('No elements found with the specified class name.')

else:
    print('Failed to fetch the webpage.')