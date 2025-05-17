# Travellin AI ✈️🌍  
Projeto desenvolvido para **Imersão IA** da [Alura](https://www.alura.com.br/) em parceria com o [Google Gemini](https://gemini.google.com/app)

---

![Image](https://github.com/user-attachments/assets/9b2aee25-ea15-4b84-811b-85047df668ec)
<br><br>
![Image](https://github.com/user-attachments/assets/4ad2c22a-fcdf-4bc5-91a8-15e5f955fd30)

---

## 💡 Sobre o projeto

**Travellin AI** é um assistente de viagens inteligente que usa inteligência artificial para ajudar pessoas a descobrirem **destinos ideais**, com base no **orçamento**, **época do ano**, **preferências pessoais** e até o **clima da cidade de destino**.  
Tudo isso com uma interface responsiva e moderna, integrada com **Google Gemini 1.5 Flash** via backend em **Python com FastAPI**.

---

## Funcionalidades

- 💬 Chat com IA especializada em viagens
- 🌤️ Consulta de clima de locais de destino
- 🧳 Sugestões baseadas em data, estilo de viagem e orçamento
- ✨ Interface moderna com chips de sugestões rápidas
- ✅ IA responde apenas sobre turismo, hospedagens, clima e roteiros

---

## Por que esse projeto é valioso?

> Travellin AI não é só um chatbot — é um **planejador de viagens inteligente**.

### ✔️ Valor para usuários:
- Descobrem **destinos compatíveis com o bolso**
- Evitam horas pesquisando em sites separados
- Recebem recomendações diretas e objetivas

### ✔️ Valor como projeto técnico:
- Demonstra uso **real e útil de IA generativa**
- Integração completa frontend + backend
- UX moderna com responsividade e interatividade
- Base sólida para expansão com APIs externas

---

## 🛠 Tecnologias Utilizadas

<p align="left">
  <img alt="Python" title="Python" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
  <img alt="JavaScript" title="JavaScript" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" />
  <img alt="HTML" title="HTML" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" />
  <img alt="CSS" title="CSS" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" />
</p>

### Frontend:
- HTML5, CSS3
- JavaScript
- Google Fonts: [Clash Grotesk](https://www.fontshare.com/fonts/clash-grotesk)

### Backend:
- [FastAPI](https://fastapi.tiangolo.com/) (Python)
- [Google Gemini 1.5 Flash](https://ai.google.dev/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) para scraping de clima
- [Uvicorn](https://www.uvicorn.org/) para servidor ASGI

---

## 🚀 Como rodar localmente

### Requisitos:
- Python 3.10+
- Chave da API do Google Gemini (`GOOGLE_API_KEY`)

### Passo a passo:

## 1. Clone o repositório
```bash
git clone https://github.com/thiago-ribeiro1/Travellin-AI.git
```

## 2. Configurar a Chave API nas Variáveis de Ambiente
Configure a sua chave API como uma variável de ambiente no sistema:

#### **No Windows:**
1. Abra o **Executar** (`Win + R`), digite `sysdm.cpl` e pressione **Enter**.
2. Vá até a aba **Avançado** e clique em **Variáveis de Ambiente**.
3. Em **Variáveis do Sistema**, clique em **Novo**.
4. No campo **Nome da variável**, insira: `GOOGLE_API_KEY`.
5. No campo **Valor da variável**, insira sua chave API do Gemini.
6. Clique em **OK** e feche todas as janelas.

#### **No Linux/Mac:**
1. Abra o terminal.
2. Digite o seguinte comando e pressione **Enter**:
   ```sh
   export GOOGLE_API_KEY="SUA_CHAVE_DA_API"
   ```
3. Para tornar a variável permanente, adicione a linha acima ao arquivo `~/.bashrc` ou `~/.zshrc`.

## 3. Abra o projeto no Visual Studio Code, e crie um arquivo .env no diretório raiz com sua chave API Gemini, seguindo esse exemplo:
```bash
GOOGLE_API_KEY="sua_chave_aqui"
```

## 4. Instale todas as dependências
```bash
cd backend
pip install fastapi uvicorn python-dotenv google-generativeai beautifulsoup4 requests
cd ..
```

## 5. Rode o servidor
```bash
python backend/main.py
```
