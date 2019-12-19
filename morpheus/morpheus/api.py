from flask import request, url_for, jsonify
import requests
import json


### API von coinmarketcap.com
# globalURL - Allgemeine Infos wie z.B. Marketcap und Volumen aller Kryptowährungen zusammen
globalURL = "https://api.coinmarketcap.com/v1/global/"
# tickerURL - Coinspezifische Infos wie z.B. Marketcap und Volumen von Bitcoin
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

### API von coincecko.com
# exchangeURL - Infos zu Kryptowährungsbörsen wie z.B. Marketcap und Volumen von Binance
exchangeURL = "https://api.coingecko.com/api/v3/exchanges"

### TICKER URL
# Daten aus tickerURL beziehen
api_request = requests.get(tickerURL)
api = json.loads(api_request.content)

### EXCHANGE URL
# Daten aus exchangeURL beziehen
api_request_exchange = requests.get(exchangeURL)
api_exchange = json.loads(api_request_exchange.content)