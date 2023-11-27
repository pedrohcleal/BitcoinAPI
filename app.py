from flask import Flask, jsonify, render_template
import requestp1, json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo!'

@app.route('/details/<address>')
def adress(address):
    print('/details/<address>')
    info_btc = requestp1.get_bitcoin_address_info(address)

    if info_btc:
        
        return render_template('detalhes_template.html', json_response=info_btc)
    else:
        return jsonify({"erro": "Não foi possível obter os detalhes do endereço"}), 500

@app.route('/balance/<address>')
def pagina3(address):
    print('/details/<address>')
    info_btc = requestp1.balance(address)

    if info_btc:
        
        return render_template('detalhes_template.html', json_response=info_btc)
    else:
        return jsonify({"erro": "Não foi possível obter os detalhes do endereço"}), 500


@app.route('/send/<address>')
def pagina4(nome):
    return f'Olá, {nome}!'

@app.route('/txt/<txt>')
def pagina5(txt):
    return f'Olá, {txt}!'

if __name__ == '__main__':
    app.run(debug=True)

