import requests
import json

dict_info = {}

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
        data_utxos = data["txrefs"]
        contador = 0 
        con_uncof = 0

        for x, valor in enumerate(data_utxos):
            value1 = float(json.dumps(data_utxos[x]["value"]))
            confirmation = json.dumps(data_utxos[x]["confirmations"])
            if float(confirmation) >= 2:
                contador += value1
            else:
                con_uncof += value1

            #print(contador)

        resultado_json = {"confirmed": contador, "unconfirmed": con_uncof}

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
    if dict_info.get(t_id) != None:
        print("retornou o dict sem fazer req na api")
        return dict_info[t_id]

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

        dict_info[t_id] = dict_tx

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
if __name__ == "__main__":
    address = "bc1q788t5fz0nm3zkn9z8rnqy5sxqlkgsejdr0zry2"
    str_tx = "3780357508784f95a729bd7bde7b4fd78328f46ef693ae7fa921afac4136137d"
    info = info_tx(address)
    print(balance(address))