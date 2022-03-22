from flask import Flask, request, Response, jsonify
import json
from blinkDetector import blinkDetector

# Váriaveis configuráveis
with open("json/config.json") as json_data_file:
    config = json.load(json_data_file)

# Declaração do servidor principal
videoServer = Flask(__name__)  # Iniciando um servidor HTTP na máquina local
bd = blinkDetector()

# Rotas
@videoServer.route('/')  # Rota padrão
def index():
    return 'videoServer'  # Verificação de funcionamento da rota

# Rota para o processamento de vídeo
@videoServer.route('/video_feed', methods=['POST'])
def video_feed():
    # Retorna o video processado
    return Response(bd.generate(request.form["image"]), mimetype="multipart/x-mixed-replace; boundary=frame")


@videoServer.route('/variaveis')  # Rota para atualização das variaveis
def variaveis():
    return bd.variaveis()


# Inicialização dos serviços
if __name__ == '__main__':

    # Configuração do servidor d query
    videoServer.debug = True

    # Inicialização do servidor de query
    videoServer.run(port=config["ports"]["videoPort"])
