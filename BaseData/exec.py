from pydantic import BaseModel
from BaseData.ControlPath import ControlPath

id = ControlPath.randomNumber()
class ObjData(BaseModel):
    id: int
    estacao: str
    end: str

class OperatorClass():

    @classmethod
    def write(id, objData:ObjData): # ESCREVER
        try:
            ControlPath.data(objData)
            print('Dado cadastrado com sucesso.')
        except:
            print('Erro de cadastro')

    @classmethod
    def update(objData:ObjData, id=False): # EDITAR
        if id == True:
            ControlPath.update_data(id, objData)
        else:
            print("Necessário passar um ID e um Objeto")

    @classmethod
    def read(id, data):
        try:
            ControlPath.filterElement(id or data)
        except:
            print('Dado não encontrado.')

    @classmethod
    def delete(id, data):
        try:
            ControlPath.delete_data(id or data)
            print('Dado deletado com sucesso')
        except:
            print('Erro ao deletar')






