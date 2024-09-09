from ControllerClass.ClassWebScraping import ControllerAPI
import re

class Rotas:
    @staticmethod
    def methodPostIdCli(itens: list):
        try:
            request = ControllerAPI(itens.site, itens.url, itens.pathInput, itens.pathBtn, itens.pathTag)
            return request.verificarDados()
        except:
            return 'Host não encontrado!'


