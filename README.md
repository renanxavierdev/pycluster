# Distributed Systems - PyCluster


**PyCluster** é um sistema distribuído de consulta de palavras chaves dentro de um determinado arquivo de txt. Sua base é construída sobre a framework Django que auxilia na manipulação dos hosts e interface de busca. 
**PyCluster** é um trabalho acadêmico com a finalidade explorar a distribuição de informações visando processar grande volume de informações.

![enter image description here](https://raw.githubusercontent.com/renanxavierdev/pycluster/master/img/home.png)

# Requirements

Para utilização do PyCluster faz-se necessário a instação das ferramentas a seguir:

Python 2.7
Django 1.11
Pip 2

Run commands

    pip install requests
    pip install Werkzeug
    pip install pusher
    pip install psutil

## Config Real-time Pusher

Configure o pusher no server.py na raiz do projeto e view.py no modulo master>server.

Cadastre-se no pusher para ter acesso ao serviço de push:
[Clique aqui para acessar o site oficial do pusher](https://pusher.com)

    pusher_client = pusher.Pusher(
      app_id='sua_api_id',
      key='sua_key',
      secret='sua_secret',
      cluster='us2',
      ssl=True
    )


## Run Project

Para iniciar o projeto starte o django (Master)

    ./manage.py runserver seu_ip:8000

Inicie o servidor em cada maquina que irá fazer o processamento. (Slave)

    python server.py


## Create Host
Cadastre os hosts para a comunicação com o master. Porta padrão dos server: é**4000**

![enter image description here](https://github.com/renanxavierdev/pycluster/raw/master/img/Dashboard.png)

## Search
Funcionamento do PyCluster

Resultado do processamento
![Busca](https://github.com/renanxavierdev/pycluster/raw/master/img/search.png)

 - O **cliente** acessa a pagina index fazendo o upload do arquivo txt e inserindo as palavras chaves.
 - **Master** Faz a quebra do arquivo, divide para os servers e envia-os com uma thread.
 - **Servers** processam a informação fazendo a contagem das ocorrências encontradas e retornam para o master


![Diagrama](https://github.com/renanxavierdev/pycluster/raw/master/img/diagram.png)


## Contributions

[Victor Queiroz](https://github.com/Victor-Queiroz)
[Daniel Carvalho](http://github.com/danielcarv)

## License

Copyright 2018 Renan Xavier

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
