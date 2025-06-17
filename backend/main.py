import os
import webbrowser
import requests
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from dotenv import load_dotenv
import google.generativeai as genai
from bs4 import BeautifulSoup

# Ambiente
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Config Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

# FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Onde estão index.html, css/, js/, img/
ROOT = Path(__file__).parent.parent

# Montar estáticos
app.mount("/css", StaticFiles(directory=ROOT / "css"), name="css")
app.mount("/js", StaticFiles(directory=ROOT / "js"), name="js")
app.mount("/img", StaticFiles(directory=ROOT / "img"), name="img")

# Servir página
@app.get("/")
def index():
    return FileResponse(ROOT / "index.html")

# Utilitários
def get_city_from_ip(ip: str) -> str:
    try:
        return requests.get(f"http://ip-api.com/json/{ip}").json().get("city", "")
    except:
        return ""

def obter_clima_google(cidade: str) -> str:
    try:
        q = f"clima agora em {cidade}".replace(" ", "+")
        r = requests.get(f"https://www.google.com/search?q={q}&hl=pt-BR",
                         headers={"User-Agent": "Mozilla/5.0"})
        s = BeautifulSoup(r.text, "html.parser")
        tm = s.find("span", {"id": "wob_tm"})
        dc = s.find("span", {"id": "wob_dc"})
        loc = s.find("div", {"id": "wob_loc"})
        if tm and dc and loc:
            return f"{loc.text}: {tm.text}°C, {dc.text}"
    except:
        pass
    return "Clima não definido."

# Chatbot 
@app.post("/chat")
async def chatbot(request: Request):
    body = await request.json()
    pergunta = body.get("message", "")
    ip = request.client.host
    cidade = get_city_from_ip(ip)
    clima = obter_clima_google(cidade) if cidade else "Localização não detectada."

    # Instruções
    prompt = f"""
    Você é um agente de viagens profissional e foi treinado para responder de forma clara, definitiva e sucinta **exclusivamente** sobre:

    - Destinos turísticos
    - Clima em determinadas regiões
    - Roteiros e atrações
    - Hospedagens, hotéis e orçamentos de viagem
    - Épocas ideais para visitar certos lugares
    - Valores de passagens aéreas
    - Valores de hotéis e pacotes de viagem
    - Informações sobre o clima atual
    - Informações sobre o clima em regiões específicas
    - Quero viajar sozinho
    - Férias em família com crianças

    Se o usuário perguntar algo **fora desse contexto**, responda de forma educada:
    "Fui treinado para responder apenas sobre viagens, destinos, hospedagem e clima."
    O usuário disse: "{pergunta}"
    Localização do usuário: {cidade}
    Clima atual: {clima}

    Responda com texto direto, claro e sucinto, com tom objetivo. Evite listas, HTML e markdown. 
    """

    # Adiciona a pergunta do usuário
    try:
        resp = chat.send_message(prompt)
        text = resp.text.strip()

        # Remover blocos ```html ou ```
        if text.startswith("```html"):
            text = text.replace("```html", "", 1).strip()
        if text.startswith("```"):
            text = text.replace("```", "", 1).strip()
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0].strip()

        return {"response": text}

    except Exception as e:
        print("Erro ao enviar para Gemini:", e)
        return {"response": "A IA atingiu o limite de uso. Tente novamente em instantes."}

# Run
if __name__ == "__main__":
    webbrowser.open("http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
