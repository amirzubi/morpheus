from flask import Flask
from flask import render_template
from flask import request

import requests
import json

# API von coinmarketcap.com
globalURL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

# Daten aus der globalURL
request = requests.get(globalURL)
data = request.json()
globalMarketCap = data['total_market_cap_usd']

app = Flask("Cryptocurrency Portfolio")
    
@app.route("/portfolio/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Gesamte Marktkapitalisierung: " + globalMarketCap
        return rueckgabe_string
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)