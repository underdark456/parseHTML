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

tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
no_tags = tag_re.sub('', user_input)

# file = open('C:/Users/igor.shavrov/Documents/1.txt', 'w+')
# for row in test.findAll('tr'):
#     cells = row.findAll("td")
#     print (cells[:2])
#     try:
#         file.write(str(cells[:2])+'\n')
#     except:
#         print("TT")
#         print(cells[:2])



#pickle.dump(str(cells), file)
file.close()

# try:
#     file = pickle.load(open('C:/Users/igor.shavrov/Documents/htmlString.p', 'rb'))
#     if file == test:
#         print ('Values not changed!')
#         sys.exit(0)
#     else:
#         pickle.dump (test, open ('C:/Users/igor.shavrov/Documents/htmlString.p', 'wb'))
#         print ('Saving')
# except IOError:
#     pickle.dump(test,open('C:/Users/igor.shavrov/Documents/htmlString.p', 'wb'))
#     print('Created new file.')

# file = open('C:/Users/igor.shavrov/Documents/i.txt','r')
# for row in file:
#     file = row
# print(file)
#
# i = 0
# for row in test.find_all('tr'):
#     try:
#         col = re.findall('<td>(.{10})', str(row))
#         print(col[0])
#         if str(file) == str(col[0]):
#             print("Обновка не требуется")
#         else:
#             print("Дата не соответствует. Качаем новый файл")
#         break
#     except Exception:
#         continue
#

    #col = row.search('<td>(.{10})')
    #col = re.search('.*', row)
    #print(col)
    #print(col.group(1))

#column_1 = col[0].string.strip()
#date.append(column_1)

# tds = test.find_all('td')


# # print(test)
# datasets = []
# for row in test.find_all('tr'):
#   z = row.find_all('td')
#
# print(z)

