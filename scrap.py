import requests
from bs4 import BeautifulSoup
import webbrowser as wb
def extract_href_links(url):
    try:
        # Fetch the web page content
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> elements and extract their href attributes
        href_links = [a.get('href') for a in soup.find_all('a')]

        return href_links
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
url = 'https://www.google.com/search?q=square root java codezclub'
href_links = extract_href_links(url)

# # if href_links:
# # #     # Print the extracted href links
for i, link in enumerate(href_links, 1):
    print(f"Link {i}: {link}")
# else:
#      print("No href links were extracted.")