"""
Scraping Wikipedia h2 Headers

Used the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python.

Tasks:
- Download the HTML of the Page
- Parse all `<h2>` section headers.
- Store the clean header titles in a list.
- Print the total count and display the first 10 section titles.

Handle the network errors gracefully.
"""
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Stranger_Things"

def get_h2_headers(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    print(h2_tags)
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
        headers.append(header_text)
    
    for h in headers:
        print(h)


get_h2_headers(URL)