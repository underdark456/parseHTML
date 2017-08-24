import requests
import re
from bs4 import BeautifulSoup
import pickle
import pandas

s = requests.Session()
r = s.get('http://lk.fcsm.ru')
soup = BeautifulSoup(r.text,'html.parser')
v = soup.find("input", attrs={"name" : "__RequestVerificationToken"})['value'] #Token harvest

login = s.post('http://lk.fcsm.ru/Account/Login?ReturnUrl=%2FHome%2FIndex',cookies=r.cookies, data = {'__RequestVerificationToken' : v, 'UserName' : 'backoff@qbfin.ru', 'Password' : 'UHje7piU'})
itog = s.get('http://lk.fcsm.ru/Home/Incoming/backoff%40qbfin.ru', cookies=r.cookies)
itog.encoding = 'UTF-8'

soup_task = BeautifulSoup(itog.text,'html.parser')


test = soup_task.find("table",{"class": "table-layout"})


file = open('C:/Users/igor.shavrov/Documents/1.txt', 'w+')
for row in test.findAll('tr'):
    cells = row.findAll("td")
    print (cells[:2])
    try:
        file.write(str(cells[:2])+'\n')
    except:
        print("TT")
        print(cells[:2])
    file.close()
