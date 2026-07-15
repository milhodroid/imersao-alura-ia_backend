# Importando o FastAPI para criar a aplicação e HTTPException para erros HTTP
from fastapi import FastAPI, HTTPException

# Criando a instância principal da aplicação FastAPI
app = FastAPI()

# Definindo o endpoint GET na rota raiz "/"
@app.get("/")
def hello_world():
    # Retorna uma mensagem de saudação em formato JSON
    return {"mensagem": "Olá, mundo! 🌍"}

# Lista central de figurinhas (usada pelos dois endpoints abaixo)
figurinhas = [
    {"id": 1, "nome": "Neo",      "categoria": "THE MATRIX - 1999"},
    {"id": 2, "nome": "Morpheus", "categoria": "THE MATRIX - 1999"},
]

# Definindo o endpoint GET na rota "/figurinhas"
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista completa de figurinhas em formato JSON
    return figurinhas

# Definindo o endpoint GET na rota "/figurinhas/{figurinha_id}"
@app.get("/figurinhas/{figurinha_id}")
def buscar_figurinha(figurinha_id: int):
    # Percorre a lista procurando a figurinha com o id informado
    for figurinha in figurinhas:
        if figurinha["id"] == figurinha_id:
            return figurinha
    # Se não encontrou, lança o erro 404 com uma mensagem clara
    raise HTTPException(status_code=404, detail=f"Figurinha com id {figurinha_id} não encontrada.")
