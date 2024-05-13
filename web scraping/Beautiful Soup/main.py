from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'html.parser')
    h2_tags = soup.find_all('div',class_='job-posting')
    for h2_tag in h2_tags:
        job_title = h2_tag.h2.text
        job_location = h2_tag.find('div',class_='location').text
        print("\033[92m" + "Title: " + "\033[0m" + job_title)
        print("\033[92m" + "Location: " + "\033[0m" + job_location)
        print("\033[92m"+"###############"+ "\033[0m")