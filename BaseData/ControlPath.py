from random import random

import os
import json

class ControlPath:
    @classmethod
    def __createdir(self): #CRIA PASTA
        try: 
            os.makedirs("data")
            print("Diretório Criado com sucesso.")
        except OSError:
            if not os.path.isdir("data"):
                raise Exception("Diretório criado com sucesso.")
            
    @classmethod  
    def __cratefile(self): #CRIA ARQUIVO
        try:
            os.path.isfile("/data/database.json")
            with open('./data/database.json', 'x') as f:
                f.write(json.dumps([], indent=4))
                print("O arquivo criado com sucesso.")
        except OSError:
           if not os.path.exists("data"):
            raise Exception("O arquivo criado com sucesso.")

    @classmethod
    def __readFile(self): #LEITURA DO ARQUIVO
       with open('./data/database.json', 'r', encoding='utf-8-sig') as readFile:
            try:
                return json.load(readFile)
            except:
                print ("Será criado uma nova lista")
                return readFile.read() 
            
    @classmethod
    def __writeFile(self, data): #ESCRITA NO ARQUIVO
        with open('./data/database.json', 'w', encoding='utf-8-sig') as writeFile:
            writeFile.write(json.dumps(data, indent=4))

    #RECRIA PASTA E ARQUIVO SE FOREM DELETADOS
    @classmethod
    def data(self, data):
        if os.path.isdir('data') == False or os.path.isfile('./data/database.json') == False:
            self.__createdir() or self.__cratefile()

        arrFilter = self.filterArr(item=data)
        verify = self.checkList(data=data)
        if verify != None and arrFilter == None:
            self.__writeFile(verify)
        pass
  
    @classmethod
    def checkList(self, data=None): #VERIFICA SE EXISTE DADOS NO ARRAY
        #VEIRFICA SE EXISTE DADOS
        ArrayList = []
        fileJson = self.__readFile()
        if type(fileJson) == str:
            ArrayList.append(data)
            return ArrayList
        else:
            fileJson.append(data)
            return fileJson
    
    @classmethod
    def deleta_data(self, item=None): #DELETA DADOS NO ARRAY
        fileJson = self.__readFile()
        lst = self.filterElement(item)
        print(lst)
        if lst != None:
            fileJson.remove(lst)
            self.__writeFile(fileJson)
        else:
            print('Item não exste!')
        pass
        
#listaStorage.splice(listaStorage.findIndex(itens => itens.username === username),1);
    ##########SECTION FILTER##########
    @classmethod
    def filterArr(self, item=None): #FILTER SE EXISTEM DADOS JÁ CADASTRADOS NO ARRAY
            try:
                fileJson = self.__readFile()
                if item != None: #FILTRA SE EXISTE ARRAY IGUAL
                    filter = [arr for arr in fileJson if arr == item]
                    if len(filter) > 0:
                        return fileJson
            except:
                return None
        
    @classmethod
    def filterElement(self, item): #FILTER VERIFICA SE EXISTE DADOS NO ARRAY
s

    ##########SECTION RANDON NUMBER##########          
    @classmethod
    def randomNumber(self):
        nunber = self.filterElement(int((random())*1000))
        while nunber == True:
            return int((random())*1000)
        return int((random())*1000)