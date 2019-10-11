from flask import Flask
from flask import render_template
from flask import request

import requests
import json

app = Flask("Morpheus") 

# API von coinmarketcap.com
globalURL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

# Daten aus der globalURL beziehen
request = requests.get(globalURL)
data = request.json()
globalMarketCap = data['total_market_cap_usd']
    
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", globalMarketCap=globalMarketCap)

if __name__ == "__main__":
    app.run(debug=True, port=5000)