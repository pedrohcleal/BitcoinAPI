import requests
import json

def get_bitcoin_address_info(address):
    url = "https://api.blockcypher.com/v1/btc/main/addrs/{}".format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
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
        return resultado_json
    else:
        return "O endereço de bitcoin está inválido : Erro {}".format(response.status_code)

def balance(address):
    url = "https://api.blockcypher.com/v1/btc/main/addrs/{}".format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        resultado_json = (
            '{\n'
            f'  "confirmed": "{data["final_balance"]}",\n'
            f'  "unconfirmed": "{data["unconfirmed_balance"]}"\n'
            '}\n'
        )
        return resultado_json
    else:
        return "O endereço de bitcoin está inválido : Erro {}".format(response.status_code)
    
def escolher_utxos(address):
    url = "https://api.blockcypher.com/v1/btc/main/addrs/{}".format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        utxos = []
        resultado_json = data["txrefs"]
        for indice, tx in enumerate(data["txrefs"]):
            utxos.append({"txid":resultado_json[indice]["tx_hash"],
                          "amount":resultado_json[indice]["value"]})

        dict_utxo = {"utxos":utxos}
        return json.dumps(dict_utxo,indent=2)
    else:
        return "O endereço de bitcoin está inválido : Erro {}".format(response.status_code)
    
def info_tx(t_id):
    url = "https://api.blockcypher.com/v1/btc/main/txs/{}".format(t_id)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        data_outputs= data["outputs"]
        list_address = []

        for indice, tx in enumerate(data_outputs):
            list_address.append({"address":data_outputs[indice]["addresses"][0],
                                 "value":data_outputs[indice]["value"]})
        
        dict_tx = {"addresses": list_address, 
                   "block": data["block_height"],
                   "txID": data["hash"] }
        
        return json.dumps(dict_tx,indent=2)
    else:
        return "ID de transação está inválido : Erro {}".format(response.status_code)

def health():
    url = "https://api.blockcypher.com/v1/btc/main/"
    response = requests.get(url)
    if response.status_code == 200:
        return "A API está operacional, status code: {}".format(response.status_code)
    else:
        return "A API não está opericioanl\nErro {}".format(response.status_code)

# Realizar testes das funções
"""if __name__ == "__main__":
    address = "de6d495ede6dbb072861ec38609dd065182ef784e1bc20bc7c1df651f404b0f7"
    info = info_tx(address)
    print(info)"""