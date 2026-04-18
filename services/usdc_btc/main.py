##########################################################

import requests 
import json

# Valor inicial
# 0.00028148 = 72858 = 20.50

# Valor final
# 0.00028148 = 71.093 = x 

# Calc 
# % = ((Valor final - Valor incial) / valor incial) * 100

#btc_usc = 0.0000137253 # preço no momento da compra 1 / BTC
#btc_price = 1 / (btc_usc)
# print(btc_price)
usdcAmmount = 0

wallet = [{'date' : '2026-04-08', 'price' : 1 / (0.0000137253), 'currency' : 'USD', 'usdcAmmount' : 20.50870926,'cType' : 'BTC', 'cAmmout' : 0.00028148, 'initialValue' : 0.00028148 * 72858}, {'date' : '2026-04-15', 'price' : 1 / (0.0000134623), 'currency' : 'USD', 'usdcAmmount' : 26.42138372,'cType' : 'BTC', 'cAmmout' : 0.00035569, 'initialValue' : 0.00035569 * 74281}]

##########################################################3

# Getting de quote 

url = 'https://economia.awesomeapi.com.br/last/BTC-USD'


# Requisição GET
response = requests.get(url)
data = response.json()
print("COTAÇÃO BTC COMPRA EM USDC", (data['BTCUSD']['bid']))

passed = float(data['BTCUSD']['bid'])
intBTC = int(passed)

appreciation = 0
lucro = 0
total_invest = 0

for c in wallet:
    lenght_wallet = len(wallet)
    # Capturando valor investido individualmente com loop for
    uniqueUSDC = c['usdcAmmount']
    # inicial - atual
    total_invest += c['usdcAmmount']
    initialCurrency = c['initialValue']
    finalCurrency = c['cAmmout'] * intBTC
    # calculo entre total investido e % de valorização / devalorização 
    print(f"USDC {finalCurrency:.2f}, {uniqueUSDC:2f}")
    lucro += (finalCurrency - uniqueUSDC) 
    appreciation = (lucro / total_invest) * 100
    print(f"TOTAL INVEST DE {total_invest:.2f}")
    print(f"LUCRO DE {lucro:.2f}")
    print(f"VALORIZAÇÃO DE {appreciation:.2f}% VALOR FINAL NA CARTEIRA DE {((total_invest * (appreciation / 100)) + total_invest):.2f}")
    


# print(wallet[0]['date'])
# print(f"LENG DE DADOS CARTEIRA LOOP FOR {len(wallet)}")

