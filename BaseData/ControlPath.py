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
        with open('./data/database.json', 'w') as writeFile:
            writeFile.write(json.dumps(data, indent=4))


    #RECRIA PASTA E ARQUIVO SE FOREM DELETADOS
    @classmethod
    def data(self, data):
        if os.path.isdir('data') == False or os.path.isfile('./data/database.json') == False:
            self.__createdir() or self.__cratefile()

        verify = self.checkList(data=data)
        arrFilter = self.filterArr(data=data)
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
        if type(fileJson) == list:
            fileJson.append(data)
            return fileJson
    '''   
    @classmethod
    def deleta_data(self, data=None):
        verify = self.filterElement(data)
        fileJson = self.__readFile()
        if (verify != None):
            print(fileJson)
            print(data)
        pass
    '''


    @classmethod
    def filterArr(self, data=None): #FILTER SE EXISTEM DADOS JÁ CADASTRADOS NO ARRAY
        with open('./data/database.json', 'r') as readFile:
            try:
                fileJson = json.load(readFile)
                if data != None: #FILTRA SE EXISTE ARRAY IGUAL
                    filter = [arr for arr in fileJson if arr == data]
                    if len(filter) > 0:
                        return fileJson
            except:
                return None
        
    @classmethod
    def filterElement(self, data=None): #FILTER VERIFICA SE EXISTE DADOS NO ARRAY
        with open('./data/database.json', 'r') as readFile:
            fileJson = json.load(readFile)
            if data != None: #FILTRA SE EXISTE ELEMENTO IGUAL NO ARRAY
                for key in fileJson:
                    for value in key:
                        if key[value] == data:
                            return key[value]
'''
    @classmethod
    def filterValue(self, data=None):
        if data != None: #FILTRA SE EXISTE ELEMENTO IGUAL
                for x in self.__readFile():
                    if data['site'] == x['site']:
                        print('Existe dados')
                    else:
                        return True
'''

