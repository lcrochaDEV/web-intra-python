from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ControlRequest.ClassRequest import Rotas
from BaseData.ControlPath import ControlPath

class ObjModel(BaseModel):
   site: str
   url: str
   pathTag : str

n = ControlPath.randomNumber()
#print(n)

data = {
    "id": "",
    "site": "site233.com",
    "url": "https://site112.com/gerador-nomes-pessoas",
    "pathTag": "//span[@class='d-table-cell v-align-middle lh-condensed pr-2']//strong"
}

def methods(data:ObjModel):
    ControlPath.data(data)
    #ControlPath.delete_data(item="site233.com2")
methods(data)

class Update(BaseModel):
    key: str
    value: str

update = {"site": "NovoSite.com.br"}

def Up(id, update:Update):
    ControlPath.update_data(id, update)
Up(3, update)

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

