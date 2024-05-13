from bs4 import BeautifulSoup
import requests
import time

website_data = requests.get("https://www.soccerbase.com/results/home.sd").text

soup = BeautifulSoup(website_data, "html.parser")

# Extract and print titles
titles = soup.find_all("h2")
for title in titles:
    match_title = title.text.strip()
#     print(match_title)
#     print("")

# print("####################")

# Extract and print match information
def match():
    matches = soup.find_all("tr", class_="match")
    with open("match.txt", "a", encoding="utf-8") as file:
        for match in matches:
            home_team_element = match.find("td", class_="team homeTeam")
            away_team_element = match.find("td", class_="team awayTeam")
            result = match.find("td", class_="score")

            home_team = home_team_element.a.text.strip()
            away_team = away_team_element.a.text.strip()
            result_text = result.text.strip()
            file.write( home_team + " " + result_text + " " + away_team + "\n")
            #print(home_team + " " + result_text + " " + away_team)

if __name__ == "__main__":
    while True:
        match()
        hour = 24
        print("Done , it will work in next 24 Hours")
        time.sleep(hour*3600)
        