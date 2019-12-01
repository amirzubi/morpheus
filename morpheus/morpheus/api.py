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
