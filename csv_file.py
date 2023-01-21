from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://praedicoglobalresearch.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="icon-box")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['services', 'description']
    thewriter.writerow(header)

    for list in lists:
        services=list.find('h4').text.replace('\n', '')
        description=list.find('p').text.replace('\n', '')
        
        
        info = [services, description]
        thewriter.writerow(info)