from flask import Flask, jsonify, render_template, request
import requestp1, json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo!'

@app.route('/details/<address>')
def info_wallet(address):
    print('/details/<address>')
    info_btc = requestp1.get_bitcoin_address_info(address)

    if info_btc:
        
        return render_template('detalhes_template.html', json_response=info_btc)
    else:
        return jsonify({"erro": "Não foi possível obter os detalhes do endereço"}), 500

@app.route('/balance/<address>')
def balance(address):
    print('/details/<address>')
    info_btc = requestp1.balance(address)

    if info_btc:
        
        return render_template('detalhes_template.html', json_response=info_btc)
    else:
        return jsonify({"erro": "Não foi possível obter os detalhes do endereço"}), 500


@app.route('/send', methods=['POST'])
def send_btc():
    data = request.json
    endereco_destino = data.get('send_address')
    quantidade_btc = data.get('qtd_btc')
    info_utxo = requestp1.escolher_utxos(endereco_destino)
    print("solicitação antedida")
    if (info_utxo):
        return render_template('detalhes_template.html', json_response=info_utxo)
    else:
        return jsonify({"erro": "Não foi possível obter os detalhes do endereço"}), 500

@app.route('/tx/<tx>')  #https://api.blockcypher.com/v1/btc/main/txs
def pagina5(tx):
    info_txn = requestp1.info_tx(tx)

    if (info_txn):
        return render_template('detalhes_template.html', json_response=info_txn)
    else:
        return jsonify({"erro": "Não foi possível obter os detalhes do endereço"}), 500


if __name__ == '__main__':
    app.run(debug=True)

