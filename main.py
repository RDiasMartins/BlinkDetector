from flask import Flask, render_template
from threading import Thread
import json
import os

#Variaveis do programa
#Declaração do servidor principal
mainServer = Flask(__name__)

# Váriaveis configuráveis
with open("json/config.json") as json_data_file:
    config = json.load(json_data_file)

#Rotas
@mainServer.route('/')#HOME
def index():
    return render_template("index.html")

@mainServer.route('/visualizar')#Visualização dos itens cadastrados
def visualizarTemplate():
    return render_template("crudVisualizar.html")

@mainServer.route('/cadastrar')#Visualização dos itens cadastrados
def cadastrar():
    return render_template("crudCadastrar.html", queryPort = config["ports"]["queryPort"])

#Threads dos outros serviços
class queryServer(Thread):#Serviço gerenciador de banco de dados
    def run(self):
        os.system('python py/queryServer.py')

class videoServer(Thread):#Serviço processamento de imagens
    def run(self):
        os.system('python py/videoServer.py')

#Inicialização dos serviços
if __name__ == '__main__':
    #Inicialização dos outros serviços
    queryServer().start()
    videoServer().start()

    #Configuração do servidor principal
    mainServer.debug = True

    #Inicialização do servidor principal
    mainServer.run(host = "0.0.0.0", port = config["ports"]["mainPort"]);
