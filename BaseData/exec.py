from pydantic import BaseModel
from BaseData.ControlPath import ControlPath

class ObjData(BaseModel):
    id: int
    sitecode: str
    end: str

class OperatorClass():

    @staticmethod
    def write(sitecode = None, end = None): # ESCREVER
        try:
            ControlPath.data({"id": ControlPath.randomNumber(), "sitecode": sitecode, "end": end})
            return 'Dado cadastrado com sucesso.'
        except:
            return 'Erro de cadastro'

    @staticmethod
    def update(objData:ObjData, id=False): # EDITAR
        if id == True:
            ControlPath.update_data(id, objData)
            return 'Dado cadastrado com sucesso.'
        else:
            return "Necessário passar um ID e um Objeto"

    @classmethod
    def read(self, id=None, data=None):
        try:
            return ControlPath.filterElement(id or data)
        except:
            return 'Dado não encontrado.'

    @classmethod
    def delete(self, id=None, data=None):
        try:
            ControlPath.delete_data(id or data)
            return 'Dado deletado com sucesso'
        except:
            return 'Erro ao deletar'






