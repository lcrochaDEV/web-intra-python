from ControllerClass.ClassWebScraping import ControllerAPI
from BaseData.exec import OperatorClass

class Rotas:
    @staticmethod
    def methodPostIdCli(itens: list):
        try:
            valor = OperatorClass.read(data=itens.site)
            if not valor:
                data = ControllerAPI.varrerDados(itens.site, itens.url, itens.pathInput, itens.pathBtn, itens.pathTag1, itens.pathTag2)
                OperatorClass.write(itens.site, data)
                return OperatorClass.read(data=itens.site)
            else:
                return valor
        except:
            return 'Host não encontrado!'


