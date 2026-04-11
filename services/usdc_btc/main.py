##########################################################

btc_usc = 0.0000137253
btc_price = 1 / (btc_usc)
usdcAmmount = 20.50870926

wallet = {'date' : '2026-04-08', 'price' : btc_price, 'currency' : 'USD', 'usdcAmmount' : usdcAmmount,'Ctype' : 'BTC', 'Ctpye_ammout' : 0.00028148}

##########################################################3

# Getting de quote 

import requests 
import json


url = 'https://economia.awesomeapi.com.br/last/BTC-USD'


# Requisição GET
response = requests.get(url)
data = response.json()
print(data['BTCUSD']['bid'])
print(wallet['price'])

