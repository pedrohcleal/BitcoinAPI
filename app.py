from flask import Flask, jsonify, render_template, request
import requestp1, json

app = Flask(__name__)

@app.route('/')
def index():
    return 'app.py -> Online'

@app.route('/health')
def info_health():
    check = requestp1.health()
    return render_template('detalhes_template.html', json_response=check)

@app.route('/details/<address>')
def info_wallet(address):
    info_btc = requestp1.get_bitcoin_address_info(address)
    return render_template('detalhes_template.html', json_response=info_btc)

@app.route('/balance/<address>')
def balance(address):
    info_btc = requestp1.balance(address)
    return render_template('detalhes_template.html', json_response=info_btc)

@app.route('/send', methods=['POST'])
def send_btc():
    data = request.json
    endereco_destino = data.get('send_address')
    quantidade_btc = data.get('qtd_btc')
    info_utxo = requestp1.escolher_utxos(endereco_destino)
    return render_template('detalhes_template.html', json_response=info_utxo)

@app.route('/tx/<tx>')  
def pagina5(tx):
    info_txn = requestp1.info_tx(tx)
    return render_template('detalhes_template.html', json_response=info_txn)

if __name__ == '__main__':
    app.run(debug=True)