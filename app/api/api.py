from fastapi import FastAPI
from pydantic import BaseModel

from app.orquestrar.orquestração import OrchestrateEmilia

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
    storage_orchestrator = OrchestrateEmilia(text)
    return storage_orchestrator
