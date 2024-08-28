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
    def __readFile(self, format=False): #LEITURA
       with open('./data/database.json', 'r', encoding='utf-8-sig') as readFile:
            try:
                return json.load(readFile)
            except json.JSONDecodeError:
                print ("Será criado uma nova lista")
                return readFile.read() 
            
    @classmethod
    def __writeFile(self, data): #ESCREVER
        with open('./data/database.json', 'w') as writeFile:
            writeFile.write(json.dumps(data, indent=4))

    @classmethod
    def data(self, data):
        try:
            with not self.__createdir() and not self.__cratefile():
               pass
        except:
            verify = self.checkList(data=data)
            arrFilter = self.filterArr(data=data)
            if verify != None and arrFilter == None:
                self.__writeFile(verify)
            pass

    @classmethod
    def checkList(self, data=None): #VERIFICA SE EXITE DADOS NO ARRAY
        #VEIRFICA SE EXITE DADOS
        ArrayList = []
        fileJson = self.__readFile()
        if type(fileJson) == str:
            ArrayList.append(data)
            return ArrayList
        if type(fileJson) == list:
            fileJson.append(data)
            return fileJson

    @classmethod
    def filterArr(self, data=None): #LEITURA
        with open('./data/database.json', 'r') as readFile:
            try:
                fileJson = json.load(readFile)
                if data != None: #FILTRA SE EXITE ARRAY IGUAL
                    filter = [arr for arr in fileJson if arr == data]
                    if len(filter) > 0:
                        return fileJson
            except:
                return None
        
    @classmethod
    def filterElement(self, data=None): #LEITURA
        with open('./data/database.json', 'r') as readFile:
            fileJson = json.load(readFile)
            if data != None: #FILTRA SE EXITE ELEMENTO IGUAL NO ARRAY
                for key in fileJson:
                    for value in key:
                        if key[value] == data:
                            return key[value]




'''
        with open('./data/database.json', 'r') as readFile:
                if readFile == True:
                    fileJson = json.load(readFile)
                    print(readFile)
                else:
                    return False
'''

'''
            if readFile == False:
            fileJson = json.load(readFile)
                for x in fileJson:
                    if data['site'] == x['site']:
                        print('Existe dados')
            if data != None: #FILTRA SE EXITE ELEMENTO IGUAL
                for x in fileJson:
                    if data['site'] == x['site']:
                        print('Existe dados')
                    else:
                        return True
            elif filterArr != None: #FILTRA SE EXITE ARRA IGUAL
                for x in fileJson:
                    return x
            elif filterElement != None: #FILTRA SE EXITE ELEMENTO IGUAL NO ARRAY
                for dataJson in fileJson:
                    for value in dataJson:
                        if dataJson[value] == filterElement:
                            return dataJson[value]
            else:
                return False
            
'''         