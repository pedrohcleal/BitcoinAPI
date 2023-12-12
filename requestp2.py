import requests
import json
 
def get_bitcoin_address_info(address):
    url = "https://api.blockcypher.com/v1/btc/main/addrs/{}".format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        resultado_json = {
            "address": data["address"],
            "balance": str(data["balance"]),
            "totalTx": data["n_tx"],
            "balanceDetails": {
                "confirmed": str(data["final_balance"]),
                "unconfirmed": str(data["unconfirmed_balance"])
            },
            "total": {
                "sent": str(data["total_sent"]),
                "received": str(data["total_received"])
            }
        }
        return resultado_json
    else:
        return "O endereço de bitcoin está inválido : Erro {}".format(response.status_code)

def balance(address):
    url = "https://api.blockcypher.com/v1/btc/main/addrs/{}".format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        resultado_json = (
            {"confirmed": {data["final_balance"]},
            "unconfirmed": {data["unconfirmed_balance"]}}
        )
        return resultado_json
    else:
        return "O endereço de bitcoin está inválido : Erro {}".format(response.status_code)
    
def escolher_utxos(address, amount):
    """
    Seleciona os UTXOS necessários para pagar uma transação.

    Args:
        address: O endereço da carteira de Bitcoin.
        amount: O valor a ser transferido.

    Returns:
        Uma lista de objetos UTXO.
    """
    token = "inserir token blockcypher"
    url = "https://api.blockcypher.com/v1/btc/main/addrs/{}/unspents?token={}".format(address,token)
    response = requests.get(url)
    unspents = response.json()

    # Inicializa a lista de UTXOS selecionados.
    selected_utxos = []

    # Percorre a lista de UTXOS não gastos.
    for utxo in unspents:
        # Se o valor do UTXO for maior ou igual ao valor restante da transação, adiciona o UTXO à lista de UTXOS selecionados.
        if utxo["value"] >= amount:
            selected_utxos.append(utxo)
            amount -= utxo["value"]
            # Se o valor restante da transação for zero, pare o algoritmo.
        if amount == 0:
            break

        return json.dumps(selected_utxos,indent=2)
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
        return "A API não está opericional\nErro {}".format(response.status_code)

# Realizar testes das funções
"""if __name__ == "__main__":
    address = "de6d495ede6dbb072861ec38609dd065182ef784e1bc20bc7c1df651f404b0f7"
    info = info_tx(address)
    print(info)"""