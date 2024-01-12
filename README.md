# Backend Test

Este desafio visa criar uma aplicação em Flask que disponibiliza endpoints de API para obter informações sobre endereços Bitcoin, saldos, transações e seleção de UTXO para envio de bitcoins.

## Estrutura do Projeto

### Arquivos Principais

- **app.py:** O arquivo principal contendo a lógica da aplicação Flask e a definição dos endpoints da API.
- **requestp1.py:** Um módulo contendo funções que realizam solicitações à API BlockCypher para obter informações sobre endereços Bitcoin e transações.

### Endpoints da API

1. **GET /health:**
   - Retorna o status de saúde da API.

   **Exemplo de Retorno:**
   ```json
   "A API está operacional, status code: 200"
   ```

2. **GET /details/{address}:**
   - Recebe um endereço Bitcoin como parâmetro e retorna informações detalhadas sobre o endereço em formato JSON, conforme especificado no desafio.

   **Exemplo de Retorno:**
   ```json
   {
    "address": "bc1qyzxdu4px4jy8gwhcj82zpv7qzhvc0fvumgnh0r",
    "balance": "0",
    "totalTx": 251243,
    "balance": {
        "confirmed": "0",
        "unconfirmed": "0"
    },
    "total": {
        "sent": "665978870281",
        "received": "665978870281"
      }
   ```

3. **GET /balance/{address}:**
   - Recebe um endereço Bitcoin como parâmetro e retorna o saldo confirmado e não confirmado com base nos UTXOs associados a esse endereço, em formato JSON, conforme especificado no desafio.

   **Exemplo de Retorno:**
   ```json
   {
    "confirmed": "1312321321321",
    "unconfirmed": "12321321"
   }
   ```

4. **POST /send:**
   - Recebe dados JSON contendo um endereço de destino e a quantidade de bitcoins a serem enviados.
   - Seleciona os UTXOs necessários para realizar o envio.
   - Retorna os UTXOs selecionados em formato JSON, conforme especificado no desafio.

   **Exemplo de Retorno:**
   ```json
   {
     "utxos": [
       {
         "txid": "9ec20061fc37196c2ca689c36b002b786d461ee054a0557793be1eba11163932",
         "amount": "17880859"
       },
       {
         "txid": "ee95bfb4a45c8e388447c2873893bc4c5aaee5083d0436017d3ae2bd6d0c38b9",
         "amount": "729049"
       },
       ...
     ]
   }
   ```

5. **GET /tx/{tx}:**
   - Recebe um ID de transação como parâmetro e retorna as informações sobre os endereços e a quantidade de bitcoin que cada endereço recebeu na transação, em formato JSON, conforme especificado no desafio.

   **Exemplo de Retorno:**
   ```json
   {
    "addresses": [
      {
        "address": "bc1puzeuw22z55e64wl2rwvajslks665w7u5mlymz8lzy5j8tkldmlzqxslpla",
        "value": 7016948
      },
      {
        "address": "bc1qdpz9q8khp8klhw50aveynj53ea5vg433u952j8",
        "value": 263366
      }
    ],
    "block": 818912,
    "txID": "0535da4665c697fe17940a77323864c52d287ab89c13094a706efc277d8df9fe"
   }
   ```

## Como Executar

### Clone o repositório
1. **Abra o terminal na pasta onde deseja clonar o repositório.**

2. **Execute o seguinte comando para clonar o repositório:**

   ```bash
   git clone https://github.com/pedrohcleal/Desafio-Klever.git
   ```

3. **Após a conclusão do clone, entre no diretório do projeto:**

   ```bash
   cd Desafio-Klever
   ```

4. **Ativando o Ambiente Virtual**

```bash
# Ative o ambiente virtual
# No Windows
venv\Scripts\activate

# No Linux/Mac
source venv/bin/activate
```

Ao ativar o ambiente virtual, o prompt de comando ou terminal deve mostrar o nome do ambiente virtual, indicando que está ativo.

5. **Executando o `app.py`**

Certifique-se de estar no diretório do seu projeto no terminal e que o ambiente virtual está ativado.

```bash
# Execute o app.py
python app.py
```

O Flask iniciará o servidor e estará pronto para receber solicitações.

6. **Acessando os Endpoints**

Com o servidor em execução, você pode acessar os endpoints da API no navegador ou usando ferramentas como o Postman.

Por exemplo:
- [http://localhost:5000/health](http://localhost:5000/health)
- [http://localhost:5000/details/{address}](http://localhost:5000/details/{address})
- [http://localhost:5000/balance/{address}](http://localhost:5000/balance/{address})
- [http://localhost:5000/send](http://localhost:5000/send)
- [http://localhost:5000/tx/{tx}](http://localhost:5000/tx/{tx})

Lembre-se de substituir `{address}` e `{tx}` pelo endereço de carteiras de Bitcoin e IDs de transações respectivamente.

7. **Desativando o Ambiente Virtual**

Quando terminar de usar o aplicativo, desative o ambiente virtual:

```bash
# No Windows
deactivate

# No Linux/Mac
source deactivate
```

Ao desativar o ambiente virtual, o prompt de comando ou terminal deve retornar ao ambiente global.

Certifique-se de ajustar os comandos de acordo com o seu sistema operacional. Essas instruções assumem que você está usando um terminal padrão ou o PowerShell no Windows.

## Testando com Postman

Para testar o endpoint de envio de bitcoins ("/send") usando o Postman:

1. Selecione a solicitação como POST.
2. Insira a URL: `http://localhost:5000/send`.
3. Selecione a guia "Body" e escolha a opção "raw" para inserir dados JSON.
4. Insira dados JSON de exemplo no corpo da solicitação:
   ```json
   {
     "send_address": "bc1qyzxdu4px4jy8gwhcj82zpv7qzhvc0fvumgnh0r",
     "qtd_btc": 0.1
   }
   ```
5. Envie a solicitação e veja a resposta.

### Postman
![Exmplo](https://i.imgur.com/ueyWQFr.png)
