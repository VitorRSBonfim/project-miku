# Getting de quote 

import requests 
import json

url = 'https://economia.awesomeapi.com.br/last/BTC-USD'


# Requisição GET
response = requests.get(url)
data = response.json()
print(data['BTCUSD']['bid'])

