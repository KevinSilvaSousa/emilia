from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ApiRequests(BaseModel):
    mensagem: str
    usuario: str
    contexto_conversa: list[str]

@app.get("/home")
def homepage():
    return {"Hello": "Word"}


@app.post("/chat")
def chat_response(text: ApiRequests):
    pass