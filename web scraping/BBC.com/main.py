import requests
from bs4 import BeautifulSoup
import time
import json

# Constants
URL = "https://www.bbc.com/burmese/topics/c404v08p1wxt"
OUTPUT_FILE = "bbc_burmese.json"

def get_soup(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None

def scrape_bbc_burmese():
    soup = get_soup(URL)
    if not soup:
        return

    data = []
    cards = soup.find_all("li", class_="bbc-t44f9r")
    for card in cards:
        post_time = card.find("time", class_="promo-timestamp bbc-11pkra2 e1mklfmt0").text.strip()
        post_name = card.find("a", class_="focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0").text
        post_image = card.find("img", class_="bbc-139onq")['src']  # Getting the src attribute
        post_detail_link = card.find("a", class_="focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0")['href']  # Getting the href attribute

        data.append({
            "Post Title": post_name,
            "Post Image": post_image,
            "Post Time": post_time,
            "More Link": post_detail_link
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:  # Use mode "w" to overwrite the file each time
        json.dump(data, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    while True:
        scrape_bbc_burmese()
        waiting_minutes = 60
        print(f"Results saved in the file. It will work again in the next {waiting_minutes} minutes.")
        time.sleep(waiting_minutes * 60)
