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

        arrFilter = self.filterArr(data)
        verify = self.checkList(data)
        if verify != None and arrFilter == None:
            self.__writeFile(verify)
      
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
    def delete_data(self, item=None): #DELETA DADOS NO ARRAY
        fileJson = self.__readFile()
        lst = self.filterElement(item) #FILTRA POR NOME OU ID
        if lst != None:
            fileJson.remove(lst)
            self.__writeFile(fileJson)
        else:
            print('Item inexistente!')

    @classmethod
    def update_data(self, id=None, data=None): #UPDATE DADOS NO ARRAY
        new_list = self.filterElement(id) #FILTRA POR NOME OU ID
        new_list[list(dict.keys(data))[0]] = list(dict.values(data))[0]
        try:
            if dict.keys(new_list) == dict.keys(new_list):
                for l in dict.keys(new_list):
                    if list(dict.keys(data))[0] == l:
                        if self.filterArr(new_list) == None:
                            self.delete_data(id)
                            self.data(new_list)
                            print('Atualizado com Sucesso!')
                            pass
                        else:
                            print('Dado existente.')
        except:
            print('Item não encontado na lista.')

        pass

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
        fileJson = self.__readFile()
        if item != None: #FILTRA SE EXISTE ELEMENTO IGUAL NO ARRAY
            if type(item) == int or type(item) == str:
                for lst in fileJson:
                    for key in lst:
                        if lst[key] == item:
                            return lst

    ##########SECTION RANDON NUMBER##########          
    @classmethod
    def randomNumber(self):
        nunber = self.filterElement(int((random())*1000))
        while nunber == True:
            return int((random())*1000)
        return int((random())*1000)