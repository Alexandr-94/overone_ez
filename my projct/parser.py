import requests   # библиотека для HTTP запросов
from bs4 import BeautifulSoup  # библиока для парсинга сайта
#
# url = "https://select.by/kurs/"
#
# headers = {
#     "accept":"*/*",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
with open('index.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, features="html.parser")
all_valuta = soup.find_all('tr', class_="text-center h4")
#print(all_valuta)
all_text2 = []
all_text3 = []

for all in all_valuta:
    all_text = all.text
    all_text2.append(all_text)
h = ''
for i in all_text2:
    for j in i:
        if j == '\n':
            continue
        else:
            h += j
    all_text3.append(h)
    h = ''
print(all_text3)
for i in all_text3:

    print(i)
# usd = str(all_text3[0])
# eur = all_text3[1]
# ru_rub = all_text3[2]
# zlot = all_text3[3]
# griv = all_text3[4]
# print(usd,'\n',eur,'\n',ru_rub,'\n',zlot,'\n',griv,'\n')
#print(all_text2)
#print(all_text3)


