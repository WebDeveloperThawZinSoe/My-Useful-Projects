from bs4 import BeautifulSoup
import requests
import time

def myfun():
    html_data = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=Industry&from=submit&clubJob=n&cboIndustry=27&gadLink=IT-Hardware/Networking").text

    soup = BeautifulSoup(html_data, 'html.parser')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = f"job_results_{timestamp}.txt"

    with open(filename, "a") as file:
        for job in jobs:
            company_name = job.find('h3', class_='joblist-comp-name')
            key_skill = job.find('span', class_='srp-skills')
            job_title = job.find('h2').find('a')
            file.write("Company Name: " + company_name.text.strip() + "\n")
            file.write("Job Title: " + job_title.text.strip() + "\n")
            file.write("Key Skill: " + key_skill.text.strip() + "\n")
            file.write("################\n")

if __name__ == "__main__":
    while True:
        myfun()
        print(f"Results saved in the file. It will work again in the next 1 minute.")
        time.sleep(10)
