import requests
import json

def get_bitcoin_address_info(address):
    
    url = "https://api.blockcypher.com/v1/btc/main/addrs/{}".format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # Criar um dicionário combinando os dados
        resultado_json = (
            '{\n'
            f'    "address": "{data["address"]}",\n'
            f'    "balance": "{data["balance"]}",\n'
            f'    "totalTx": {data["n_tx"]},\n'
            '    "balance": {\n'
            f'        "confirmed": "{data["final_balance"]}",\n'
            f'        "unconfirmed": "{data["unconfirmed_balance"]}"\n'
            '    },\n'
            '    "total": {\n'
            f'        "sent": "{data["total_sent"]}",\n'
            f'        "received": "{data["total_received"]}"\n'
            '    }\n'
            '}\n'
        )
        print(resultado_json)
        
        return resultado_json
    else:
        return response.status_code

def balance(address):
    
    url = "https://api.blockcypher.com/v1/btc/main/addrs/{}".format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # Criar um dicionário combinando os dados
        resultado_json = (
            '{\n'
            f'  "confirmed": "{data["final_balance"]}",\n'
            f'  "unconfirmed": "{data["unconfirmed_balance"]}"\n'
            '}\n'
        )
        print(resultado_json)
        
        return resultado_json
    else:
        return response.status_code
    

if __name__ == "__main__":
    address = "bc1qyzxdu4px4jy8gwhcj82zpv7qzhvc0fvumgnh0r"
    info = get_bitcoin_address_info(address)
    print(info)
