from bs4 import BeautifulSoup
import requests

website_url = "https://www.myanmar123.com/two-d"

website_data = requests.get(website_url).text

soup = BeautifulSoup(website_data, "html.parser")
datas = soup.find_all("tr")
for data in datas:
    date = data.find("td")
    time = data.find("td", class_="text-center")
    number = data.find("td", class_="font-30 text-center text-danger")
    if date:
        if time:
            if number:
                print(date.text)  # Print text content of <td>
                print(time.text)  # Print text content of <td>
                print("\033[92mNumber : {} \033[0m".format(number.text))  # Print text content of <td>
                print("\033[92m---------------------------\033[0m")
