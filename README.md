# Desafio-Klever
Endpoint para transações em Bitcoin

# Teste de Backend

## Introdução
Olá, você está pronto para a contratação?

### Por que Bitcoin?
Bitcoin foi a primeira implementação de blockchain. Um dos novos mecanismos criados por Satoshi Nakamoto foi a tecnologia da "cédula digital", que permite que ela seja transformada em "transações gastas", que são um tipo de cédula digital. Cada uma dessas cédulas pode ter um valor variável, de 1 satoshi (0.00000001 BTC) até 1.000.000 BTC.

### Como fazer um envio?
Para transferir Bitcoin de uma conta para outra, o primeiro passo é verificar as cédulas que sua conta possui e calcular a partir delas se a transação é possível, ou seja, se você tem Bitcoins suficientes (BTC). Depois disso, você deve escolher quais cédulas usar para realizar esta transação.

Por exemplo, se você tiver 3 notas de $20 e 4 notas de $50 e quiser pagar 80 dólares, você pode pegar 1 nota de $50 e 2 notas de $20 para fazer o pagamento. Se você observar, ainda sobra um troco chamado "troco".

### Melhorar a seleção de UTXO
Existem muitas maneiras de escolher quais cédulas usar em uma transação, algumas mais simples e outras mais complexas, mas qual é o objetivo que todas buscam alcançar? O Bitcoin, sendo uma rede descentralizada, exige que todas as transações sejam validadas por pelo menos 51% dos mineradores na rede, ou seja, deve haver um consenso entre eles. Para que haja um consenso, é necessário um alto nível de gastos de processamento, que pode ser menor se sua transação for menor, ou seja, tiver menos bytes. Para atingir esse objetivo, deve-se selecionar o menor número possível de UTXOs para uma transação.

## Teste de Backend 2 - O Desafio
1. A aplicação fornecerá um ponto de extremidade de API ("/details/{address}") que receberá um endereço Bitcoin e retornará os dados do endereço Bitcoin.

Este ponto de extremidade deve organizar os dados como este JSON:
```json
{
  "address": "bc1qyzxdu4px4jy8gwhcj82zpv7qzhvc0fvumgnh0r",
  "balance": "144011754",
  "totalTx": 17000,
  "balance": {
    "confirmed": "1321321",
    "unconfirmed": "123213"
  },
  "total": {
    "sent": "1189163719343",
    "received": "1189307731097"
  }
}
```

2. A aplicação fornecerá um ponto de extremidade de API ("/balance/{address}") que receberá um endereço Bitcoin e calculará o saldo Confirmado/Não Confirmado com base na lista de UTXO (saídas de transações não gastas) para esse endereço.

Se "confirmações" < 2, o "valor" deve considerar o Saldo Não Confirmado; caso contrário, deve considerar o Saldo Confirmado.

Este ponto de extremidade deve organizar os dados como este JSON:
```json
{
  "confirmed": "1312321321321",
  "unconfirmed": "12321321"
}
```

3. A aplicação fornecerá um ponto de extremidade de API ("/send") que receberá um endereço Bitcoin e a quantidade de BTC que você deseja enviar e selecionará o UTXO necessário para fazer este envio funcionar.

## Teste de Backend 3
Este ponto de extremidade deve organizar os dados como este JSON:
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

4. A aplicação fornecerá um ponto de extremidade de API ("/tx/{tx}") que receberá um ID de transação e calculará os endereços e quanto Bitcoin cada endereço recebeu na transação fornecida.

Este ponto de extremidade deve organizar os dados como este JSON:
```json
{
  "addresses": [
    {
      "address": "bc1qyzxdu4px4jy8gwhcj82zpv7qzhvc0fvumgnh0r",
      "value": "10000000"
    },
    ...
  ],
  "block": 675674,
  "txID": "3654d26660dcc05d4cfb25a1641a1e61f06dfeb38ee2279bdb049d018f1830ab"
}
```

Este é um retorno de uma lista de endereços que gastaram/receberam dinheiro nesta transação.

## Regras
- É necessário validar o endereço Bitcoin fornecido e o ID da transação.
- Você pode escolher entre HTTP ou GRPC para este Desafio.
- Adicione um ponto de extremidade de verificação de status de saúde.

## Teste de Backend 4 - Testes de Unidade/Integração
- Use BigInt para manipulações de valor.

## Valores de Exemplo
- Endereço: bc1qyzxdu4px4jy8gwhcj82zpv7qzhvc0fvumgnh0r
- Transação: 3654d26660dcc05d4cfb25a1641a1e61f06dfeb38ee2279bdb049d018f1830ab

## Endpoints do Blockbook
- **Detalhes do Endereço:** [https://bitcoin.blockbook.chains.klever.io/api/v2/address/{address}](https://bitcoin.blockbook.chains.klever.io/api/v2/address/{address})
- **Detalhes do UTXO do Endereço:** [https://bitcoin.blockbook.chains.klever.io/api/v2/utxo/{address}](https://bitcoin.blockbook.chains.klever.io/api/v2/utxo/{address})
- **Detalhes da Transação:** [https://bitcoin.blockbook.chains.klever.io/api/v2/tx/{tx}](https://bitcoin.blockbook.chains.klever.io/api/v2/tx/{tx})
