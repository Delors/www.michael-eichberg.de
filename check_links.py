import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def check_links(file_path):
    # Read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # Find all links
    links = soup.find_all('a', href=True)

    # Check each link
    for link in links:
        url = link['href'] 
        parsed_url = urlparse(url)
        
        # Check if the URL has a scheme
        if not parsed_url.scheme:
            print(f"No scheme: {url}")
            continue
            
        try:
            print(f"Checking: {url}", end=' ')
            response = requests.head(url, allow_redirects=True)
            if response.status_code == 200:
                print(f"Valid")
            else:
                print(f"Invalid (Status code: {response.status_code})")
        except requests.RequestException as e:
            print(f"Error: {url} ({e})")

# Path to your HTML file
print("Checking teaching.html")
check_links('teaching.html')
print("Checking projects.html")
check_links('projects.html')
print("Checking publications.html")
check_links('publications.html')