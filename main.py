# Importando o FastAPI para criar a aplicação e HTTPException para erros HTTP
from fastapi import FastAPI, HTTPException

# Importando FileResponse para servir arquivos diretamente ao cliente
from fastapi.responses import FileResponse

# Importando CORSMiddleware para liberar acesso cross-origin (frontend <-> backend)
from fastapi.middleware.cors import CORSMiddleware

# Importando os para manipulação de caminhos de arquivos do sistema operacional
import os

# Importando glob para buscar arquivos por padrão de nome na pasta de imagens
import glob

# Criando a instância principal da aplicação FastAPI
app = FastAPI()

# Configurando o middleware CORS para aceitar requisições de qualquer origem
# Isso é necessário para que o frontend (rodando em outra porta/domínio) consiga
# se comunicar com este servidor sem ser bloqueado pelo navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Aceita qualquer origem
    allow_credentials=True,
    allow_methods=["*"],       # Aceita qualquer método HTTP (GET, POST, etc.)
    allow_headers=["*"],       # Aceita qualquer cabeçalho
)

# Definindo o caminho absoluto da pasta base (onde este arquivo está localizado)
# Isso garante que o servidor encontre a pasta independente de onde for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))

# Definindo o caminho absoluto da pasta de imagens das figurinhas
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista central de figurinhas com id, nome, categoria, descricao e URL da imagem.
# Os dados (nomes, categorias, descrições) são fiéis ao index.html do frontend.
# imagem_url aponta para o endpoint dedicado que serve o arquivo via FileResponse.
# Figurinhas comentadas ainda não têm imagem disponível na pasta figurinhas/.
figurinhas = [

    # ── THE MATRIX (1999) ─────────────────────────────────────────────────────
    # Página 1 — Personagens Principais
    {"id": 1,  "nome": "Neo",            "categoria": "THE MATRIX · 1999",         "descricao": "Thomas A. Anderson — O Escolhido",               "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2,  "nome": "Morpheus",       "categoria": "THE MATRIX · 1999",         "descricao": "Capitão do Nabucodonosor",                        "imagem_url": "/figurinhas/2/imagem"},
    # {"id": 3,  "nome": "Trinity",       "categoria": "THE MATRIX · 1999",         "descricao": "Hacker lendária e guia de Neo",                   "imagem_url": "/figurinhas/3/imagem"},
    # {"id": 4,  "nome": "Agent Smith",   "categoria": "THE MATRIX · 1999",         "descricao": "Agente do sistema — o antagonista",               "imagem_url": "/figurinhas/4/imagem"},
    # {"id": 5,  "nome": "Oracle",        "categoria": "THE MATRIX · 1999",         "descricao": "Profetisa de Zion",                               "imagem_url": "/figurinhas/5/imagem"},

    # Página 2 — Momentos Icônicos
    # {"id": 6,  "nome": "Bullet Time",          "categoria": "THE MATRIX · 1999",  "descricao": "A esquiva das balas que definiu uma era",         "imagem_url": "/figurinhas/6/imagem"},
    # {"id": 7,  "nome": "A Pílula Vermelha",    "categoria": "THE MATRIX · 1999",  "descricao": "A escolha entre a ilusão e a verdade",            "imagem_url": "/figurinhas/7/imagem"},
    # {"id": 8,  "nome": "Dojo Fight",           "categoria": "THE MATRIX · 1999",  "descricao": "Neo vs Morpheus — treinamento de kung fu",        "imagem_url": "/figurinhas/8/imagem"},
    # {"id": 9,  "nome": "Lobby Scene",          "categoria": "THE MATRIX · 1999",  "descricao": "A invasão ao edifício de aço e vidro",            "imagem_url": "/figurinhas/9/imagem"},
    # {"id": 10, "nome": "Desert of the Real",   "categoria": "THE MATRIX · 1999",  "descricao": "\"Welcome to the real world, Neo.\"",             "imagem_url": "/figurinhas/10/imagem"},

    # ── THE MATRIX RELOADED (2003) ────────────────────────────────────────────
    # Página 3 — Novos Personagens
    # {"id": 11, "nome": "Niobe",         "categoria": "RELOADED · 2003",           "descricao": "Capitã do Logos — pilota de elite",               "imagem_url": "/figurinhas/11/imagem"},
    # {"id": 12, "nome": "Ghost",         "categoria": "RELOADED · 2003",           "descricao": "Tripulante do Logos — habilidade letal",          "imagem_url": "/figurinhas/12/imagem"},
    # {"id": 13, "nome": "Os Gêmeos",     "categoria": "RELOADED · 2003",           "descricao": "Agentes fantasmas — inimigos intangíveis",        "imagem_url": "/figurinhas/13/imagem"},
    # {"id": 14, "nome": "Keymaker",      "categoria": "RELOADED · 2003",           "descricao": "Guardião das chaves do sistema",                  "imagem_url": "/figurinhas/14/imagem"},
    # {"id": 15, "nome": "Seraph",        "categoria": "RELOADED · 2003",           "descricao": "Protetor da Oracle — o anjo dourado",             "imagem_url": "/figurinhas/15/imagem"},

    # Página 4 — Cenas Épicas
    # {"id": 16, "nome": "Freeway Chase", "categoria": "RELOADED · 2003",           "descricao": "Perseguição épica na autoestrada",                "imagem_url": "/figurinhas/16/imagem"},
    # {"id": 17, "nome": "Château Fight", "categoria": "RELOADED · 2003",           "descricao": "Neo vs. guardas do Merovingiano",                 "imagem_url": "/figurinhas/17/imagem"},
    # {"id": 18, "nome": "The Architect", "categoria": "RELOADED · 2003",           "descricao": "\"Choice. The problem is choice.\"",              "imagem_url": "/figurinhas/18/imagem"},
    # {"id": 19, "nome": "Burly Brawl",   "categoria": "RELOADED · 2003",           "descricao": "Neo vs. centenas de clones de Smith",             "imagem_url": "/figurinhas/19/imagem"},
    # {"id": 20, "nome": "Club Hel",      "categoria": "RELOADED · 2003",           "descricao": "A emboscada no clube noturno",                    "imagem_url": "/figurinhas/20/imagem"},

    # ── THE MATRIX REVOLUTIONS (2003) ─────────────────────────────────────────
    # Página 5 — A Batalha Final
    # {"id": 21, "nome": "Machine City",  "categoria": "REVOLUTIONS · 2003",        "descricao": "O coração da civilização das máquinas",           "imagem_url": "/figurinhas/21/imagem"},
    # {"id": 22, "nome": "Bane / Smith",  "categoria": "REVOLUTIONS · 2003",        "descricao": "Humano corrompido pelo agente Smith",             "imagem_url": "/figurinhas/22/imagem"},
    # {"id": 23, "nome": "Cap. Mifune",   "categoria": "REVOLUTIONS · 2003",        "descricao": "Defensor de Zion — herói do APU",                 "imagem_url": "/figurinhas/23/imagem"},
    # {"id": 24, "nome": "Kid",           "categoria": "REVOLUTIONS · 2003",        "descricao": "O jovem que se libertou sozinho",                 "imagem_url": "/figurinhas/24/imagem"},
    # {"id": 25, "nome": "Rama-Kandra",   "categoria": "REVOLUTIONS · 2003",        "descricao": "Programa com amor genuíno",                       "imagem_url": "/figurinhas/25/imagem"},

    # Página 6 — O Fim da Guerra
    # {"id": 26, "nome": "Siege of Zion", "categoria": "REVOLUTIONS · 2003",        "descricao": "A batalha derradeira pela última cidade",         "imagem_url": "/figurinhas/26/imagem"},
    # {"id": 27, "nome": "Neo vs. Smith", "categoria": "REVOLUTIONS · 2003",        "descricao": "O confronto final sob a chuva",                   "imagem_url": "/figurinhas/27/imagem"},
    # {"id": 28, "nome": "Sati",          "categoria": "REVOLUTIONS · 2003",        "descricao": "Programa criança — o futuro da paz",              "imagem_url": "/figurinhas/28/imagem"},
    # {"id": 29, "nome": "Deus Ex Machina","categoria": "REVOLUTIONS · 2003",       "descricao": "O rosto da inteligência das máquinas",            "imagem_url": "/figurinhas/29/imagem"},
    # {"id": 30, "nome": "A Paz",         "categoria": "REVOLUTIONS · 2003",        "descricao": "O amanhecer sobre uma nova Matrix",               "imagem_url": "/figurinhas/30/imagem"},

    # ── THE MATRIX RESURRECTIONS (2021) ───────────────────────────────────────
    # Página 7 — O Retorno
    # {"id": 31, "nome": "Bugs",          "categoria": "RESURRECTIONS · 2021",      "descricao": "Nova Morpheus — a liberdade é real",              "imagem_url": "/figurinhas/31/imagem"},
    # {"id": 32, "nome": "The Analyst",   "categoria": "RESURRECTIONS · 2021",      "descricao": "O novo arquiteto do controle",                    "imagem_url": "/figurinhas/32/imagem"},
    # {"id": 33, "nome": "Novo Morpheus", "categoria": "RESURRECTIONS · 2021",      "descricao": "Programa gerado pelo código de Morpheus",         "imagem_url": "/figurinhas/33/imagem"},
    # {"id": 34, "nome": "Sati Adulta",   "categoria": "RESURRECTIONS · 2021",      "descricao": "Guardiã da lembrança de Neo",                     "imagem_url": "/figurinhas/34/imagem"},
    # {"id": 35, "nome": "Novo Smith",    "categoria": "RESURRECTIONS · 2021",      "descricao": "Inimigo aliado — o rogue agent",                  "imagem_url": "/figurinhas/35/imagem"},

    # Página 8 — Nova Realidade
    # {"id": 36, "nome": "Mirror World",      "categoria": "RESURRECTIONS · 2021",  "descricao": "A Matrix dentro da Matrix",                       "imagem_url": "/figurinhas/36/imagem"},
    # {"id": 37, "nome": "Bullet Time Redux", "categoria": "RESURRECTIONS · 2021",  "descricao": "O poder redescoberto de Neo",                     "imagem_url": "/figurinhas/37/imagem"},
    # {"id": 38, "nome": "Neo & Trinity",     "categoria": "RESURRECTIONS · 2021",  "descricao": "Juntos novamente — amor além do código",          "imagem_url": "/figurinhas/38/imagem"},
    # {"id": 39, "nome": "White Rabbit",      "categoria": "RESURRECTIONS · 2021",  "descricao": "O símbolo que guia para a verdade",               "imagem_url": "/figurinhas/39/imagem"},
    # {"id": 40, "nome": "Cena Final",        "categoria": "RESURRECTIONS · 2021",  "descricao": "Voando sobre uma nova Matrix",                    "imagem_url": "/figurinhas/40/imagem"},
]

# Definindo o endpoint GET na rota raiz "/"
@app.get("/")
def hello_world():
    # Retorna uma mensagem de saudação em formato JSON
    return {"mensagem": "Olá, mundo! 🌍"}

# Definindo o endpoint GET na rota "/figurinhas"
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista completa de figurinhas ativas em formato JSON
    return figurinhas

# Definindo o endpoint GET na rota "/figurinhas/{id}/imagem"
# Serve o arquivo de imagem diretamente usando FileResponse
@app.get("/figurinhas/{id}/imagem")
def imagem_figurinha(id: int):
    # Monta o padrão de busca: "{id:02d}[!0-9]*"
    # Isso encontra arquivos que começam com o número zero-padded (ex: "01")
    # seguido de qualquer caractere que NÃO seja um dígito (evita colisões entre
    # ids como 1 e 10, 2 e 20, etc.)
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")

    # Usa glob para buscar todos os arquivos que correspondem ao padrão
    arquivos = glob.glob(padrao)

    # Se não encontrou nenhum arquivo, retorna 404
    if not arquivos:
        raise HTTPException(status_code=404, detail=f"Imagem da figurinha {id} não encontrada.")

    # Retorna o primeiro arquivo encontrado como FileResponse
    # O FastAPI detecta automaticamente o media_type pelo cabeçalho do arquivo
    return FileResponse(arquivos[0])
