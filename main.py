# Importando o FastAPI para criar a aplicação
from fastapi import FastAPI

# Criando a instância principal da aplicação FastAPI
app = FastAPI()

# Definindo o endpoint GET na rota raiz "/"
@app.get("/")
def hello_world():
    # Retorna uma mensagem de saudação em formato JSON
    return {"mensagem": "Olá, mundo! 🌍"}
