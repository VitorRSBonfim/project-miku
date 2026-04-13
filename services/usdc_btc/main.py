##########################################################

import requests 
import json

# Valor inicial
# 0.00028148 = 72858 = 20.50

# Valor final
# 0.00028148 = 71.093 = x 

# Calc 
# % = ((Valor final - Valor incial) / valor incial) * 100

btc_usc = 0.0000137253 # preço no momento da compra 1 / BTC
btc_price = 1 / (btc_usc)
# print(btc_price)
usdcAmmount = 20.50870926

wallet = [{'date' : '2026-04-08', 'price' : btc_price, 'currency' : 'USD', 'usdcAmmount' : usdcAmmount,'cType' : 'BTC', 'cAmmout' : 0.00028148, 'initialValue' : 0.00028148 * 72858}]

##########################################################3

# Getting de quote 

url = 'https://economia.awesomeapi.com.br/last/BTC-USD'


# Requisição GET
response = requests.get(url)
data = response.json()
print("COTAÇÃO BTC COMPRA EM USDC", (data['BTCUSD']['bid']))

passed = float(data['BTCUSD']['bid'])
intBTC = int(passed)

finalCurrency = wallet[0]['cAmmout'] * intBTC
initialCurrency = wallet[0]['initialValue']
appreciation = ((finalCurrency - initialCurrency) / initialCurrency) * 100
final = initialCurrency + ((appreciation / 100)) * initialCurrency
# calculating the wallet variation

atual_ = wallet
# variation =

# print(wallet[0]['date'])
# print(f"LENG DE DADOS CARTEIRA LOOP FOR {len(wallet)}")

btc = wallet[0]['cAmmout'] * intBTC
print(f"{finalCurrency:.2f} {initialCurrency:.2f} {appreciation} {final:.2f}")
