from bs4 import BeautifulSoup
import requests


def getGolden():
    res = requests.get('https://www.goldlegend.com/')
    soup = BeautifulSoup(res.text,"html.parser")
    buy = soup.find_all(class_="goldprice_tw_buy")[0].text.strip()
    sell=soup.find_all(class_="goldprice_tw_sell")[0].text.strip()
    price=soup.find_all(class_="d-inline-block goldprice_bid")[0].text.strip()
    return str('國際黃金價格為，一盎司'+price+'美元，銀樓買進的黃金價格，一錢為新台幣' + buy +'元，銀樓賣出的黃金價格，一錢為新台幣' + sell+'元')

# print(getGolden())