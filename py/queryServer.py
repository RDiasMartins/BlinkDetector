from flask import Flask, request, jsonify
import json
import mysql.connector
import cv2
import numpy

#Variaveis do programa
#Declaração do servidor principal
queryServer = Flask(__name__) # Iniciando um servidor HTTP na máquina local

# Váriaveis configuráveis
with open("json/config.json") as json_data_file:
    config = json.load(json_data_file)

#Rotas
@queryServer.route('/', methods = ['GET', 'POST', 'DELETE']) # Definindo rota com o servidor em HTTP da máquina local (Nesse caso)
def index():
    conexao = mysql.connector.connect(**config["database"]) # Realizando conexão com o banco de dados
    cursor = conexao.cursor() # Objeto para execução das querys

    resultados = 0
    if request.method == 'POST': # Verifica se o metódo recebido é post
        if (request.form["operacao"] == "categorias"): # Recebe dados do formulário categoria para cadastro no DB
            #Cadastro da categoria
            nomeCategoria = request.form["nome"]

            query = "insert into categoria(nome) values('"+ nomeCategoria +"')";
            cursor.execute(query)

            #Criação no nome da imagem
            query = "select categoria_id from categoria where nome = '"+ nomeCategoria +"'";
            cursor.execute(query)

            resultados = [] # Cria lista
            for x in cursor: # Percorrendo todo o resultado da consulta (Nesse caso 1)
                resultados.append(x) # Preenche no último indice da lista

            nomeImagem = 'categoria_'+ str(resultados[0][0]) +'.png' # Concatenando o nome da imagem
        elif (request.form["operacao"] == 'objetos'):
            #Cadastro de Objeto
            nomeObjeto = request.form['nome']
            categoriaObjeto = request.form['categoria']

            query = "insert into objeto(nome, categoria_id) values ('"+ nomeObjeto +"', '"+ categoriaObjeto+"')";
            cursor.execute(query)

            #Criação no nome da imagem
            query = "select objeto_id from objeto where nome = '"+ nomeObjeto +"'";
            cursor.execute(query)

            resultados = []
            for x in cursor:
                resultados.append(x)

            nomeImagem = 'objeto_'+ str(resultados[0][0]) +'.png'

        #Salvando a imagem do objeto e a categoria
        imagem = request.files["imagem"].read() # Pega a imagem enviada pelo usuário codificiada no código do FDP (Yuri que disse)
        imagem = numpy.fromstring(imagem, numpy.uint8) # Converte a imagem em Numpy
        imagem = cv2.imdecode(imagem, 1) # Do numpy é convertida para uma imagem em openCV

        cv2.imwrite(r'static\images\\'+ nomeImagem, imagem) # Gravamento da imagem na pasta local
        conexao.commit(); # Salva todas as alterações realizadas no SQL 

        return 'ok' # Verificação de execução do script
    elif request.method == 'GET': # Método GET para visualização da lista ou slides
        if(request.args["operacao"] == "categorias"):
            query = "select categoria.categoria_id, categoria.nome from categoria;"

            cursor.execute(query)

            resultados = []
            for x in cursor:
                resultados.append(x)

            return jsonify(resultados) # Retorna em formato .JSON
        elif(request.args["operacao"] == "objetos"):
            if('categoria' in request.args): # Se o objeto tiver uma categória definida ele pega o objeto através da categoria (No caso para os slides, onde é usado exclusivamente uma categoria)
                    query = "select objeto.objeto_id, objeto.nome from objeto where objeto.categoria_id = "+request.args["categoria"]+";"

                    cursor.execute(query)

                    resultados = []
                    for x in cursor:
                        resultados.append(x)

                    return jsonify(resultados)
            else: # Nesse caso quando é a visualização em lista dos objetos
                query = "select objeto.objeto_id, objeto.nome, objeto.categoria_id, categoria.nome from objeto inner join categoria on categoria.categoria_id = objeto.categoria_id;"

                cursor.execute(query)

                resultados = []
                for x in cursor:
                    resultados.append(x)

                return jsonify(resultados)

    elif request.method == 'DELETE': # Deletar objeto da categoria
        if(request.form["tabela"] == 'categorias'):
            query = "delete from categoria where categoria_id = "+ request.form["objeto"];
            cursor.execute(query)
            conexao.commit();
        elif(request.form["tabela"] == 'objetos'):
            query = "delete from objeto where objeto_id = "+ request.form["objeto"];
            cursor.execute(query)
            conexao.commit();
        return 'ok'

#Inicialização dos serviços
if __name__ == '__main__': # É um int main() 

    #Configuração do servidor de query
    queryServer.debug = True # Atualiza automaticamente as alterações "ELE DEBUGA"

    #Inicialização do servidor de query
    queryServer.run(port = config["ports"]["queryPort"]); # Inicia o servidor
