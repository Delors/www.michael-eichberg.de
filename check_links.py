import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def check_links(file_path):
    # Read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the HTML content
    print(content)
    soup = BeautifulSoup(content, 'html.parser')

    # Find all links
    links = soup.find_all('a', href=True)

    # Check each link
    for link in links:
        url = link['href'] 
        parsed_url = urlparse(url)
        
        # Check if the URL has a scheme
        if not parsed_url.scheme:
            print(f"No scheme": {url}")
            continue
            
        try:
            response = requests.head(url, allow_redirects=False)
            if response.status_code == 200:
                print(f"Valid: {url}")
            else:
                print(f"Invalid: {url} (Status code: {response.status_code})")
        except requests.RequestException as e:
            print(f"Error: {url} ({e})")

# Path to your HTML file
file_path = 'teaching.html'
check_links(file_path)