from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# A API nao decide o que fazer com os dados ela envia sempre para o orquestrador

class ApiRequests(BaseModel):
    mensagem: str
    usuario: str
    contexto_conversa: list[str]

@app.get("/home")
def homepage():
    return {"Hello": "Word"}


@app.post("/chat")
def chat_response(text : ApiRequests):
    api_response = text
    return api_response
