import requests

# URL do servidor Flask local
url = "http://127.0.0.1:5000/send"

# Dados da solicitação
data = {
    "send_address": "bc1qyzxdu4px4jy8gwhcj82zpv7qzhvc0fvumgnh0r",
    "qtd_btc": 5
}

# Enviar solicitação POST
response = requests.post(url, json=data)

# Exibir resposta
print(response.json())
