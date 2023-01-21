from requests_html import HTMLSession
import requests

s=HTMLSession()
City=input("enter city : ")

query=City
url = f'https://www.google.com/search?q={query}+weather'
r=s.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

#->for id .->class " "->next

temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text

print(query,temp,unit,desc)


#filename="temp.txt"
#with open(filename,"w+",encoding="utf-8") as f:
#    f.write(query )
#    f.write(temp )
#    f.write(unit )
#    f.write(desc )