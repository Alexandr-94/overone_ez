import requests   # библиотека для HTTP запросов
from bs4 import BeautifulSoup  # библиока для парсинга сайта


def ticets():
    req = requests.get("https://yobit.net/api/2/ltc_btc/ticker")
    response = req.json()
    print(response)



if __name__ == '__name__':
    ticets()
