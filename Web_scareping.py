import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.example.com/"
response = requests.get(url)

# Parse the HTML response using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the desired data from the HTML
title = soup.find("title").text
body_text = soup.find("body").text

# Print the extracted data
print(title)
print(body_text)
