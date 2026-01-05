"""
Build a python script that:
1. Fetches the HN homepage (new.ycombinator.com)
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
    -Title
    -URL
4. Handles network errors and uses a clean CSV structure.
"""
import csv
import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"
CSV = "news.csv"

def get_post_links(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch: \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    post = soup.select("span.titleline > a")
    posts = []
    for link in post:
        title = link.text.strip()
        url = link.get("href").strip()
        posts.append({"title": title, "url": url})
    return posts

def save_to_csv(posts):
    if not posts:
        print("Nothing to save")
        return
    
    with open(CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url"])
        writer.writeheader()
        writer.writerows(posts)

    print(f"Saved News to {CSV}")
        

def main():
    print("Scrapping news from Hacker News portal.....")
    posts = get_post_links(URL)
    print("Saving to csv.....")
    save_to_csv(posts)

if __name__=="__main__":
    main()