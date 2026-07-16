# Importando o FastAPI para criar a aplicação e HTTPException para erros HTTP
from fastapi import FastAPI, HTTPException

# Importando StaticFiles para servir arquivos estáticos (imagens, etc.)
from fastapi.staticfiles import StaticFiles

# Importando os para manipulação de caminhos de arquivos do sistema operacional
import os

# Criando a instância principal da aplicação FastAPI
app = FastAPI()

# Definindo o caminho absoluto da pasta base (onde este arquivo está localizado)
# Isso garante que o servidor encontre a pasta independente de onde for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))

# Definindo o caminho absoluto da pasta de imagens das figurinhas
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Montando a pasta de imagens como arquivos estáticos na rota "/imgs"
# Assim, "figurinhas/01-neo.jpg" fica acessível em "/imgs/01-neo.jpg"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Definindo o endpoint GET na rota raiz "/"
@app.get("/")
def hello_world():
    # Retorna uma mensagem de saudação em formato JSON
    return {"mensagem": "Olá, mundo! 🌍"}

# Constante com o total de figurinhas do álbum completo
TOTAL_ALBUM = 40

# Lista central de figurinhas com id, nome, categoria e URL da imagem
figurinhas = [
    {"id": 1, "nome": "Neo",      "categoria": "THE MATRIX - 1999", "imagem_url": "/imgs/01-neo.jpg"},
    {"id": 2, "nome": "Morpheus", "categoria": "THE MATRIX - 1999", "imagem_url": "/imgs/02-morpheus.jpg"},
]

# Definindo o endpoint GET na rota "/figurinhas"
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista completa de figurinhas em formato JSON
    return figurinhas

# Definindo o endpoint GET na rota "/figurinhas/total"
# IMPORTANTE: deve vir ANTES de "/figurinhas/{figurinha_id}" para o FastAPI não
# confundir a palavra "total" com um figurinha_id dinâmico
@app.get("/figurinhas/total")
def estatisticas_album():
    # Calcula as figurinhas coladas a partir do tamanho atual da lista
    coladas = len(figurinhas)
    # Calcula quantas ainda faltam para completar o álbum
    faltam = TOTAL_ALBUM - coladas
    # Retorna as estatísticas calculadas dinamicamente
    return {
        "total_album": TOTAL_ALBUM,
        "coladas": coladas,
        "faltam": faltam,
    }

# Definindo o endpoint GET na rota "/figurinhas/{figurinha_id}"
@app.get("/figurinhas/{figurinha_id}")
def buscar_figurinha(figurinha_id: int):
    # Percorre a lista procurando a figurinha com o id informado
    for figurinha in figurinhas:
        if figurinha["id"] == figurinha_id:
            return figurinha
    # Se não encontrou, lança o erro 404 com uma mensagem clara
    raise HTTPException(status_code=404, detail=f"Figurinha com id {figurinha_id} não encontrada.")
