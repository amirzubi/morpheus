from flask import Flask
from flask import render_template
from flask import request

from datetime import datetime
import requests
import json

app = Flask("Morpheus")

###### API DATEN

### API von coinmarketcap.com
globalURL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

### GLOBAL URL
# Daten aus globalURL beziehen
request_globalURL = requests.get(globalURL)
data_globalURL = request_globalURL.json()
# Daten aus globalURL definieren
global_marketcap = data_globalURL['total_market_cap_usd']

### TICKER URL
# Daten aus tickerURL beziehen
request_tickerURL = requests.get(tickerURL)
data_tickerURL = request_tickerURL.json()
# Daten aus tickerURL definieren
id = data_tickerURL[0]['id']
name = data_tickerURL[0]['name']
symbol = data_tickerURL[0]['symbol']
rank = data_tickerURL[0]['rank']
price = data_tickerURL[0]['price_usd']
price_btc = data_tickerURL[0]['price_btc']
market_cap_usd = data_tickerURL[0]['market_cap_usd']
percent_change_1h = data_tickerURL[0]['percent_change_1h']
percent_change_24h = data_tickerURL[0]['percent_change_24h']
last_updated = data_tickerURL[0]['last_updated']

##### PORTFOLIO
# Portfolio Daten
portfolio_value = 0.00
last_updated = 0

# with open("portfolio.json") as portfolio:
 #   read_content = json.load(portfolio)
# portfolio_name = portfolio['id']
# portfolio_amount = portfolio['amount']


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", global_marketcap=global_marketcap )

if __name__ == "__main__":
    app.run(debug=True, port=5000)