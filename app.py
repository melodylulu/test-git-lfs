from flask import Flask, json
import oilprice,stock,aimoney,aiweather,aigolden,currency,getdata.runAIML
app = Flask(__name__) # _name_ 代表目前執行的模組

@app.route("/")  # 函式的裝飾 (Decorator): 以函式為基礎，提供附加的功能
def home():
    return 'Hello Flask test'

@app.route("/oil") # 代表我們要處理的網站路徑   "[  {    ""Result": "+oilprice.getOilPrice() +"}]"
def get_oil():
    mes =[
        {
            'result': oilprice.getOilPrice()
        }
    ]
    return   json.dumps(mes,ensure_ascii=False)

@app.route("/gold") # 黃金
def get_gold():
    mes =[
        {
            'result': aigolden.getGolden()
        }
    ]
    return   json.dumps(mes,ensure_ascii=False)

@app.route("/c/<code>") # 貨幣
def get_currency(code):
    mes =[
        {
            'result': currency.getCurrency(code)
        }
    ]
    return   json.dumps(mes,ensure_ascii=False)

@app.route("/a/<code>") # 貨幣
def get_AIML(code):
    mes =[
        {
            'result': getdata.runAIML.runAIML(code)
        }
    ]
    return   json.dumps(mes,ensure_ascii=False)


@app.route('/stock/<code>') # 股票
def get_stock(code):
    mes =[
        {
            'result': stock.getstock(code)
        }
    ]
    return  json.dumps(mes,ensure_ascii=False)

@app.route('/w/<code1>') # 天氣
def get_weather(code1):
    mes =[
        {
            'result': aiweather.getWeather(code1)
        }
    ]
    return  json.dumps(mes,ensure_ascii=False)

#@app.route('/m/<code>') #貨幣
#def get_money(code):
#    return  aimoney.getmoney(code)

if __name__=="__main__": # 如果以主程式執行
    app.run() # 立刻啟動伺服器