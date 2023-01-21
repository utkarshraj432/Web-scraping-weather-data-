import bs4
from bs4 import BeautifulSoup
import requests

url=input("enter your url : ")
response=requests.get(url)
bs=bs4.BeautifulSoup(response.text,"html.parser")
formatted_text=bs.prettify()
#print(formatted_text)

filename="temp.html"

with open(filename,"w+",encoding="utf-8") as f:
    f.write(formatted_text)

services_list=bs.find_all('div', class_='icon-box')
#print(jobs_list)
for service in services_list:
    services=service.find('h4').text
    description=service.find('p').text
    print(services)
    print(description,'\n')

