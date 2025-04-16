# Gateway SGP para Netbits

Este é um gateway que recebe requisições do SGP e as encaminha para a API da Netbits.

## Requisitos

- Python 3.8+
- Flask
- Requests
- Gunicorn

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução Local

```bash
python main.py
```

## Deploy no Railway

1. Faça login no Railway
2. Crie um novo projeto
3. Conecte com seu repositório GitHub
4. O Railway irá detectar automaticamente que é uma aplicação Python e fará o deploy 