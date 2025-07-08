
# 📊 Coletor de Cotações de Moedas para Power BI

Este script Python coleta cotações históricas das moedas **USD, EUR, JPY, CAD e GBP** frente ao Real (BRL), utilizando a [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas), e prepara os dados para uso em **relatórios Power BI**.

---

## 🚀 Funcionalidades

- Traz a cotação atual toda vez que é atualizado.
- Coleta dos últimos **90 dias** de dados de câmbio.
- Limpeza e padronização dos dados em tabelas separadas.
- Pronto para ser usado com **Power BI** via script Python.

---

<div align="center">
<img src="https://github.com/user-attachments/assets/df9b4bf9-aca8-461d-ac31-bccb661ee194" width="1000px" />
</div>

---

## ✅ Como usar no Power BI

### 1. Instale o Python (recomendado: Python 3.11)

1. Acesse: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe e instale o **Python 3.11.x (64-bit)**.
3. Durante a instalação, marque a opção:
   ```
   ✅ Add Python to PATH
   ```

---

### 2. Instale as bibliotecas necessárias

Abra o Prompt de Comando (CMD) e execute:

```bash
pip install pandas requests
```

---

### 3. Configure o Python no Power BI

1. Vá em **Arquivo > Opções e configurações > Opções**
2. Selecione **Script do Python**
3. Informe o caminho do Python instalado. Exemplo:
   ```
   C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python311
   ```

---

### 4. Execute o script no Power BI

1. Vá em **Página Inicial > Obter Dados > Script do Python**
2. Cole o seguinte código:

```python
import requests
import json
import pandas as pd

# número de dias para solicitar
dias = 90

# requisição de cada moeda pela API
usd = requests.get(f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/{dias}").json()
eur = requests.get(f"https://economia.awesomeapi.com.br/json/daily/EUR-BRL/{dias}").json()
jpy = requests.get(f"https://economia.awesomeapi.com.br/json/daily/JPY-BRL/{dias}").json()
cad = requests.get(f"https://economia.awesomeapi.com.br/json/daily/CAD-BRL/{dias}").json()
gbp = requests.get(f"https://economia.awesomeapi.com.br/json/daily/GBP-BRL/{dias}").json()

# transformar a resposta em DataFrame
dolar = pd.DataFrame(usd)
euro = pd.DataFrame(eur)
iene = pd.DataFrame(jpy)
canadense = pd.DataFrame(cad)
libra = pd.DataFrame(gbp)

# retirar colunas que não serão usadas
colunas_remover = ['code','codein','name','create_date']
dolar = dolar.drop(colunas_remover, axis=1)
euro = euro.drop(colunas_remover, axis=1)
iene = iene.drop(colunas_remover, axis=1)
canadense = canadense.drop(colunas_remover, axis=1)
libra = libra.drop(colunas_remover, axis=1)

# renomear colunas
colunas_novas = ['Máximo', 'Mínimo', 'Variação', 'Porcentagem de Variação', 'Compra', 'Venda', 'Hora da negociação']
dolar.columns = colunas_novas
euro.columns = colunas_novas
iene.columns = colunas_novas
canadense.columns = colunas_novas
libra.columns = colunas_novas

# transformar epoch em datetime
dolar['Hora da negociação'] = pd.to_datetime(pd.to_numeric(dolar['Hora da negociação']), unit='s')
euro['Hora da negociação'] = pd.to_datetime(pd.to_numeric(euro['Hora da negociação']), unit='s')
iene['Hora da negociação'] = pd.to_datetime(pd.to_numeric(iene['Hora da negociação']), unit='s')
canadense['Hora da negociação'] = pd.to_datetime(pd.to_numeric(canadense['Hora da negociação']), unit='s')
libra['Hora da negociação'] = pd.to_datetime(pd.to_numeric(libra['Hora da negociação']), unit='s')
```

3. Clique em **OK** e aguarde o carregamento das tabelas.
4. Selecione quais DataFrames importar (`dolar`, `euro`, `iene`, `canadense`, `libra`).
- Nota: os valores vem no padrão americano, faça a alteração de decimal com localidade "inglês (Estados Unidos)".
---

## 📅 Estrutura das Tabelas

Cada moeda resultará em uma tabela com as colunas:

| Coluna                   | Descrição                                      |
|--------------------------|-----------------------------------------------|
| Máximo                   | Maior valor da cotação no dia                 |
| Mínimo                   | Menor valor da cotação no dia                 |
| Variação                 | Diferença entre fechamento e abertura         |
| Porcentagem de Variação | Percentual de variação no dia                 |
| Compra                   | Cotação de compra                             |
| Venda                    | Cotação de venda                              |
| Hora da negociação       | Timestamp convertido para data/hora legível   |

---

## 📌 Fontes

- API de Moedas: [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)
- Power BI com Python: [Documentação oficial](https://learn.microsoft.com/pt-br/power-bi/connect-data/desktop-python-scripts)

---

## 🧠 Autor

**Lucas Costa**
