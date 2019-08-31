from bs4 import BeautifulSoup as bs4
import requests


def getOilPrice():
    r=requests.get('https://gas.goodlife.tw/')
    r.encoding = 'UTF-8'
    soup = bs4(r.text, 'html.parser')
    now =soup.select('div#rate li')[0].text.replace(" ", "").replace("\n","")
    rate = soup.select('div#rate li')[5].text.replace(" ", "").replace("\n","")
    b=soup.select('div#rate li')[7].text.replace(" ", "").split('\n')[1]+soup.select('div#rate li')[7].text.replace(" ", "").split('\n')[2]
    w=soup.select('div#rate li')[8].text.replace(" ", "").split('\n')[1]+soup.select('div#rate li')[8].text.replace(" ", "").split('\n')[2]
    return str(now)+'，'+str(rate)+'，'+str(b)+'，'+str(w)


#print(getOilPrice())