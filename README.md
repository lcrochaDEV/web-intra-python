### Para Instalação no Windows 10 foi criado um Ambiente Virtual

### Instalação do ambiente Virtual

```shell
python -m venv .venv
```

### Ativação do ambiente virtual no Windows

```shell
.venv/Scripts/activate
```

### Para Instalação no Debia 12 foi criado um Ambiente Virtual
 #### Crie um ambiente virtual usando venv ou virtual env Certifique-se venv de que esteja instalado executando:
```shell
sudo apt install python3-venv
```
#### Para criar um novo ambiente virtual em um **diretório chamado env**, execute:
```shell
python3 -m venv env
```
#### Para ativar este ambiente virtual (que modifica a PATH variável de ambiente), execute:
```shell
source env/bin/activate
```
#### Agora você pode instalar uma biblioteca neste ambiente virtual:
```shell
pip install XYZ
```
Os arquivos serão instalados no env/diretório.

Se quiser sair do ambiente virtual, você pode executar:
```shell
deactivate
```

### Instalação de Bibliotecas: 
```shell
#pip install selenium
#pip install python-dotenv
#pip install fastapi
#pip install "uvicorn[standard]" ou pip install "uvicorn[all]"
```
#### Iniciando o servidor Uvincorn
```shell
uvicorn app:app --reload
```

### Projeto em andamento

Este projeto visa automatizar, buscar e armazenamento de dados, ele é chamdo por metodos CRUD onde cada método verifica se existe esse dado já na base de dados JSON, caso não exista ele busca esses dados no site SMARTPLAN

#### Envio de um unico comando por http://127.0.0.1:8000/host
```json
{
    "site": "site112.com",
    "url": "https://site112.com/gerador-nomes-pessoas",
    "pathInput": "",
    "pathBtn": "",
    "pathTag": "//span[@class='d-table-cell v-align-middle lh-condensed pr-2']//strong"
}
```

### FRONT-END
#### CABEÇALHO FETCH

```js
var myHeaders = new Headers({
    'Content-Type': 'application/json',
});

let bodyObj = {
    site: '23550180',
    url: 'https://www.siterastreio.com.br/cep/2355180',
    pathInput: '//input[contains(text(), "")]',
    pathBtn: '//div[1]/div/button',
    pathTag: '/html/body/div/div[1]/main/div[2]/div[2]/div[2]/h2'
}

let conectApi = async (url, obj) => {
    var options = {
      method: "POST",
      body: JSON.stringify(obj),
      headers: myHeaders,
      mode: "cors",
      cache: "default",
    };

    try{
        const conexao = await fetch(url, options)
        if(conexao.status === 200){
            const openConexao = await conexao.json();
            return openConexao;
        } 
    }catch(error){
        console.log('Falha no link!')
    }
}

conectApi('http://127.0.0.1:8000/host', bodyObj)
```


#### Basede dados do arquivo .json
```json
{
    "id": 1,
    "sitecode": "",
    "end": ""
}
```