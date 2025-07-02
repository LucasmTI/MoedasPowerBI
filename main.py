import requests
import json
import pandas as pd

# numero de dias para solitar
dias = 90

# requisição de cada moeda pelo API
usd = requests.get(f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/{dias}").json()
eur = requests.get(f"https://economia.awesomeapi.com.br/json/daily/EUR-BRL/{dias}").json()
jpy = requests.get(f"https://economia.awesomeapi.com.br/json/daily/JPY-BRL/{dias}").json()
cad = requests.get(f"https://economia.awesomeapi.com.br/json/daily/CAD-BRL/{dias}").json()
gbp = requests.get(f"https://economia.awesomeapi.com.br/json/daily/GBP-BRL/{dias}").json()

#transformar a resposta em DataFrame
dolar = pd.DataFrame(usd)
euro = pd.DataFrame(eur)
iene = pd.DataFrame(jpy)
canadense = pd.DataFrame(cad)
libra = pd.DataFrame(gbp)

#retirar colunas que não serão usadas
dolar = dolar.drop(['code','codein','name','create_date'],axis=1)
euro = euro.drop(['code','codein','name','create_date'],axis=1)
iene = iene.drop(['code','codein','name','create_date'],axis=1)
canadense = canadense.drop(['code','codein','name','create_date'],axis=1)
libra = libra.drop(['code','codein','name','create_date'],axis=1)

# renomear colunas
dolar.columns = ['Máximo', 'Mínimo', 'Variação','Porcentagem de Variação','Compra','Venda','Hora da negociação']
euro.columns = ['Máximo', 'Mínimo', 'Variação','Porcentagem de Variação','Compra','Venda','Hora da negociação']
iene.columns = ['Máximo', 'Mínimo', 'Variação','Porcentagem de Variação','Compra','Venda','Hora da negociação']
canadense.columns = ['Máximo', 'Mínimo', 'Variação','Porcentagem de Variação','Compra','Venda','Hora da negociação']
libra.columns = ['Máximo', 'Mínimo', 'Variação','Porcentagem de Variação','Compra','Venda','Hora da negociação']

#transformar epoch em datatime
dolar['Hora da negociação'] = pd.to_datetime(pd.to_numeric(euro['Hora da negociação']), unit='s')
euro['Hora da negociação'] = pd.to_datetime(pd.to_numeric(euro['Hora da negociação']), unit='s')
iene['Hora da negociação'] = pd.to_datetime(pd.to_numeric(iene['Hora da negociação']), unit='s')
canadense['Hora da negociação'] = pd.to_datetime(pd.to_numeric(canadense['Hora da negociação']), unit='s')
libra['Hora da negociação'] = pd.to_datetime(pd.to_numeric(libra['Hora da negociação']), unit='s')
