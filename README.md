# Satisfação do Cliente em E-commerce

Projeto de análise de dados usando avaliações reais de clientes de e-commerce (dataset B2W-Reviews01), com modelagem relacional em PostgreSQL, tratamento e exploração de dados em Python, e dashboard interativo em Power BI.

## Contexto e objetivo

O projeto busca responder: o que influencia a nota que um cliente dá em uma avaliação, e essa nota se relaciona com o perfil do cliente (gênero, idade, região) ou com a marca do produto avaliado? Entender esses padrões é essencial para empresas de varejo e bens de consumo priorizarem investimentos em experiência do cliente.

## Estrutura do repositório

├── schema.sql # Criação das tabelas e índices
├── queries/ # Queries SQL documentadas
├── 01_data_cleaning.py # Tratamento e normalização dos dados brutos
├── 02_eda.ipynb # Análise exploratória de dados
├── customers.csv # Tabela de clientes (tratada)
├── products.csv # Tabela de produtos (tratada)
├── reviews.csv # Tabela de avaliações (tratada)
└── README.md

## Modelagem de dados

Os dados originais vieram em um único arquivo bruto. Foram normalizados em três tabelas relacionais:

- **customers** — dados do cliente que avaliou (id, ano de nascimento, gênero, estado)
- **products** — dados do produto avaliado (id, nome, marca, categoria)
- **reviews** — a avaliação em si (nota, recomendação, texto, sentimento)

## Ferramentas utilizadas

Python (Pandas), SQL (PostgreSQL), Power BI (DAX), Git/GitHub.

## Fonte dos dados

[B2W-Reviews01](https://github.com/b2wdigital/b2w-reviews01), disponibilizado pela B2W Digital sob licença Creative Commons BY-NC-SA 4.0.