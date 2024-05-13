from bs4 import BeautifulSoup
import requests


def ask():
    print("\033[92mEnter Your City\033[0m")
    city = input("> ")
    if city == "E":
        exit
    url = f"https://www.google.com/search?q=weather+{city}"

    website_html = requests.get(url).text
    soup = BeautifulSoup(website_html,"html.parser")
    weather = soup.find("div",class_="BNeawe iBp4i AP7Wnd").text
    print(f"{city} Tempature is {weather}")
    print("If You Want To Exsit  , Enter 'E' ")
    ask()

if __name__ == "__main__":
    ask()