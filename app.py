from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ControlRequest.ClassRequest import Rotas

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
    max_age=3600,
)

@app.get("/")
def methodGet():
   return {"API está operacional"}

class Itens(BaseModel):
   site: str
   url: str
   pathTag : str


@app.post("/host")
def methodPost(itens:Itens):
      return Rotas.methodPostIdCli(itens)

'''
@app.post("/cli")
def methodPostIdCli(itens:Itens):
      return Rotas.methodPostIdCli(itens)

@app.post("/config")
def methodPostIdConfig(itens:Itens):
      return Rotas.methodPostIdConfig(itens)
'''

