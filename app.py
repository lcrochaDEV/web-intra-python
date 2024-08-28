from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ControlRequest.ClassRequest import Rotas
from pydantic import BaseModel

from BaseData.ControlPath import ControlPath

class ObjModel(BaseModel):
   site: str
   url: str
   pathTag : str


data = {
    "id": "",
    "site": "site233.com",
    "url": "https://site112.com/gerador-nomes-pessoas",
    "pathTag": "//span[@class='d-table-cell v-align-middle lh-condensed pr-2']//strong"
}

ControlPath.data(data=data)
#verificadados = ControlPath.readFile(filterElement="site112.com")
#print(verificadados)


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
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

