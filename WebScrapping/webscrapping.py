import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the URL for Amazon (or another website) from the environment variables
url = os.getenv('coingecko_url')

# Check that the URL is being correctly retrieved (optional, can uncomment for debugging)
# print(url)

# Send a GET request to the URL and store the response in 'urlresponse'
urlresponse = requests.get(url)

# Extract the content of the response as plain text
page = urlresponse.text

# Parse the HTML content of the page using BeautifulSoup with the 'html.parser'
wanttoparse = BeautifulSoup(page, "html.parser")
print(wanttoparse)
# Create an empty list to store all the links found on the page
link_list = []

# Loop through all 'a' tags with an 'href' attribute in the parsed HTML
# for e in wanttoparse.find_all('a', href=True):
    # Optionally, print the entire anchor tag to see the elements being processed
    # print(e)

    # Append the URL (the value of 'href') to the 'link_list'
    # link_list.append(e['href'])

# Print the list of all the links found on the page
# print(link_list)