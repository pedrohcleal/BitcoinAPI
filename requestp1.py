import requests
import json
import time

address = "bc1qyzxdu4px4jy8gwhcj82zpv7qzhvc0fvumgnh0r"
url = "https://api.blockcypher.com/v1/btc/main/addrs/{}".format(address)
response = requests.get(url)


def get_bitcoin_address_info(address):
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
        #print(resultado_json)
        
        return json.dumps(data,indent=2)
    else:
        return response.status_code

def balance(address):
    if response.status_code == 200:
        data = response.json()

        # Criar um dicionário combinando os dados
        resultado_json = (
            '{\n'
            f'  "confirmed": "{data["final_balance"]}",\n'
            f'  "unconfirmed": "{data["unconfirmed_balance"]}"\n'
            '}\n'
        )
        #print(resultado_json)
        
        return resultado_json
    else:
        return response.status_code
    
def escolher_utxos(address):
    if response.status_code == 200:
        data = response.json()
        utxos = []
        # Criar um dicionário combinando os dados
        resultado_json = data["txrefs"]
        for indice, tx in enumerate(data["txrefs"]):
            
            utxos.append({"txid":resultado_json[indice]["tx_hash"],"amount":resultado_json[indice]["value"]})
            #utxos.append({"amount":resultado_json[indice]["value"]})
        
        dict_utxo = {"utxos":utxos}
        return json.dumps(dict_utxo,indent=2)
    else:
        return response.status_code
    
def info_tx(t_id):
    url = "https://api.blockcypher.com/v1/btc/main/txs/{}".format(t_id)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return json.dumps(data,indent=2)
    else:
        return response.status_code



if __name__ == "__main__":
    address = "de6d495ede6dbb072861ec38609dd065182ef784e1bc20bc7c1df651f404b0f7"
    info = info_tx(address)
    print(info)