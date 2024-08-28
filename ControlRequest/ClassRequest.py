from ControllerClass.ClassWebScraping import ControllerAPI
import re

class Rotas:
    @staticmethod
    def methodPostIdCli(itens: list):
        try:
            return ControllerAPI.varrerDados(itens.site, itens.url, itens.pathTag)
        except:
            return 'Host não encontrado!'


