# ETL de Clientes com Python
Projeto simples de ETL (Extract, Transform, Load) para o curso da DIO, que é desenvolvido em Python, utilizando um arquivo CSV local como fonte de dados. O objetivo é demonstrar, de forma prática, como ler dados brutos, aplicar transformações e salvar um novo arquivo pronto para uso. 

## Objetivo
Ler um arquivo CSV com dados de clientes contendo as colunas Nome, Conta e Cartão, aplicar limpeza e padronização, mascarar informações sensíveis e gerar um novo arquivo tratado 


## Estrutura do projeto
ETL_clientes/
├── data/
│   ├── clientes_100.csv
│   └── clientes_tratados.csv
├── extract.py
├── transform.py
├── load.py
├── main.py
└── requirements.txt

## Etapas do ETL

    ### Extract
      Leitura do arquivo CSV com as colunas:
        - Nome
        - Conta
        - Cartão

    ### Transform
        Tratamento dos dados:
        - Padronização dos nomes
        - Remoção de espaços extras
        - Remoção de duplicidades
      - Máscara nos números de cartão

    ### Load
        Gravação do resultado em um novo arquivo CSV chamado `clientes_tratados.csv`.

## Como executar

1. Instale as dependências:

    pip install -r requirements.txt


2. Execute o projeto:

    python main.py

## Exemplo de entrada

Nome,Conta,Cartão
Ana Souza,12345-6,9999-1111-2222-3333
Bruno Lima,98765-4,8888-7777-6666-5555

## Exemplo de saída

Nome,Conta,Cartão
Ana Souza,12345-6,****-****-****-3333
Bruno Lima,98765-4,****-****-****-5555

## Tecnologias utilizadas

- Python
- Pandas

## Aprendizados

Este projeto demonstra na prática como funciona um pipeline ETL local, desde a extração até a carga final dos dados tratados.