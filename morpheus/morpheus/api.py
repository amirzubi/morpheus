from flask import request, url_for, jsonify
from morpheus.forms import *
from morpheus.models import Position
import requests
import json

positions = Position.query.all()

### API von coinmarketcap.com
globalURL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

### TICKER URL
# Daten aus tickerURL beziehen
api_request = requests.get(tickerURL)
api = json.loads(api_request.content)

# Daten als neue Variable definieren
"""for x in api:
		id_ = x["id"]
		price = ("${0:.7f}".format(float(x["price_usd"])))
		symbol = x["symbol"]
		percent_change_1h = x["percent_change_1h"]
		percent_change_24h = x["percent_change_24h"]
		percent_change_7d = x["percent_change_7d"]
"""

"""
Code von Fabian Odoni (Unterricht 08.11.2019)

with open("test.json", "w") as open_file:
	json.dump(api, open_file)
"""


"""
Code von Fabian Odoni (Unterricht 08.11.2019)

def get_data():
	result = []
	for x in api:
		# if (position.name).lower() == x["id"]:
		new_position = {
			id_ : x["id"],
			symbol : x["symbol"],
			price : float(x["price_usd"]),
			percent_change_1h : x["percent_change_1h"],
			percent_change_24h : x["percent_change_24h"],
			percent_change_7d : x["percent_change_7d"],
			# value : ("${0:.2f}".format(float(position.amount * price))),
			price : ("${0:.7f}".format(float(x["price_usd"])))
		}
		result.append(new_position)
	return
"""
