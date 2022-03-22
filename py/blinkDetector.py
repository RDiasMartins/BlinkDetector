from flask import jsonify
import json
import cv2
import dlib
import imutils
from imutils import face_utils
import numpy as np
import base64
from scipy.spatial import distance as dist
import winsound
from threading import Thread
import pyttsx3
import io
from imageio import imread


class Speech(Thread):
    # Método de reprodução da voz
    def playAudio(self, answer):
        self.engine = pyttsx3.init()  # Inicializa a engine

        self.engine.setProperty('rate', 125)  # Pré define um rate

        self.engine.setProperty('volume', 1.0)  # Seta um volume padrão
        self.engine.say(answer)
        self.engine.runAndWait()

Speech().start()

# VARIAVEIS
# Váriaveis configuráveis
with open("json/config.json") as json_data_file:
    config = json.load(json_data_file)

# Classe de detecção
class blinkDetector:
    def __init__(self):
        # Variaveis do sistema
        self.acaoAnterior = "nenhuma"  # Controle da última ação
        self.acaoDefinida = "nenhuma"  # Controle da ação atual

        self.frames = 0  # Contador de frames
        self.counter = 0  # Contador de frames do olho fechado

        self.acao = []  # Vetor das piscadas

        self.nivelSlide = 0  # Nível do slide para definir as ações
        self.contadorImg = 0

        # Componentes para a detecção da piscada
        # Detector de face frontal da biblioteca DLIB
        self.detector = dlib.get_frontal_face_detector()
        # Algoritmo para definir marcas no rosto para processamento futuro
        self.predictor = dlib.shape_predictor(
            'dat/shape_predictor_68_face_landmarks.dat')

        (self.lStart, self.lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (self.rStart,
         self.rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    # Calculo do EAR (Eye Aspect Ratio)
    def eyeAspectRatio(eye):
        # Distância euclideana vertical entre os pontos p2-p6 e p3-p5
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])

        # Distância euclideana horizontal entre os pontos p1-p4
        C = dist.euclidean(eye[0], eye[3])

        # Equação do eye aspect ratio
        ear = (A + B) / (2.0 * C)

        # Retorna o eye aspect ratio
        return ear

    def esquerda(self, acaoDefinida):
        Speech().playAudio("Alexa, ligar TV")

        return acaoDefinida

    def direita(self, acaoDefinida):
        Speech().playAudio("Alexa, ligue as luzes da Sala de Estar")

        return acaoDefinida

    def confirmar(self, acaoDefinida):
        self.nivelSlide = 1
        return acaoDefinida

    def nenhumCancelar(self, acaoDefinida):
        if self.nivelSlide == 0:
            acaoDefinida = "nenhum"
        else:
            acaoDefinida = "cancelar"
            self.nivelSlide = 0

        return acaoDefinida

    def concatSeq(self, *args):
        string = ''
        for each in args:
            string += str(each)

        return string

    def readb64(self, uri):
        image = uri

        image = image.split(',')[1]

        img = imread(io.BytesIO(base64.b64decode(image)))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img

    def defineAcao(self, acao, acaoAnterior):
        # Concatenação da sequência para verificação
        sequencia = self.concatSeq(acao[0], acao[1], acao[2], acao[3], acao[4])

        # Pensar em um futuro script para gerenciar as sequências de forma prática?
        if sequencia == "10111":
            self.acaoDefinida = self.esquerda("esquerda")

        elif sequencia == "10100":
            self.acaoDefinida = self.direita("direita")

        elif sequencia == "10101":
            self.acaoDefinida = self.confirmar("confirmar")

        elif sequencia == "10110":
            self.acaoDefinida = self.nenhumCancelar("nenhumCancelar")

        acaoAnterior = self.acaoDefinida

        return self.acaoDefinida, acaoAnterior

    def generate(self, image):
        imageCam = self.readb64(image)

        # vs = cv2.VideoCapture(0)  # Inicialização da câmera

        while True:
            # ret, self.frame = vs.read()  # Captura do frame
            self.frame = imageCam

            # frameB = imutils.resize(
            #    self.frame, width=config["video"]["width"])  # Redimensionamento

            # Conversão em cinza
            #frameB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

            frameB = self.frame
            # Detecção da face dentro do frame recebido
            rects = self.detector(frameB, 0)

            for rect in rects:  # Percorre por todas as faces dentro do frame
                # Determina as marcas da face e converte em coordenadas para o numpy
                shape = self.predictor(frameB, rect)
                shape = face_utils.shape_to_np(shape)  # Conversão para o numpy

                # Extrai os dois olhos (definidos nas marcas no ínicio do algoritmo)
                leftEye = shape[self.lStart:self.lEnd]
                rightEye = shape[self.rStart:self.rEnd]

               # cv2.drawContours(frame, [leftEye], -1, (0, 255, 0), 1)

               # cv2.drawContours(frame, [rightEye], -1, (0, 255, 0), 1)

                # EAR dos olhos
                leftEAR = blinkDetector.eyeAspectRatio(leftEye)
                rightEAR = blinkDetector.eyeAspectRatio(rightEye)

                EAR = (leftEAR + rightEAR) / 2

                # Detecção da piscada
                # EAR Tresholding - olho fechado
                if EAR < config["EAR"]["Tresholding"]:
                    self.counter += 1  # Conta os frames do olho fechado

                # Olho aberto
                else:
                    self.counter = 0

                # Definição da ação
                if (len(self.acao) < 5):  # Caso a ação não tenha sido definida completamente

                    # Caso o olho esteja fechado por mais da metade do tempo de seleção da ação
                    if (len(self.acao) < 1):
                        if (self.counter > int(config["acao"]["delay"]/2)):
                            self.acao.append(1)
                            winsound.Beep(523, 100)

                    # Caso o tempo de seleção tenha acabado
                    if (self.frames == 5):

                        # Caso o olho esteja fechado por mais da metade do tempo de seleção da ação
                        if (self.counter < int(config["acao"]["delay"]/2)):
                            self.acao.append(0)
                            winsound.Beep(523, 100)

                        else:  # Caso contrário
                            self.acao.append(1)
                            winsound.Beep(523, 100)

                        self.frames = 0

                    # Começa a contar os frames a partir da primeira ação
                    if (len(self.acao) >= 1):
                        self.frames += 1

                    # Checa assinatura de comando
                    if(len(self.acao) == 3):
                        if (self.acao[0] != 1 or self.acao[1] != 0 or self.acao[2] != 1):
                            winsound.Beep(698, 300)

                            self.acao = []
                            self.frames = 0
                            cv2.waitKey(config["acao"]["delay"] * 33)
                else:  # Caso a ação tenha sido definida
                    self.acaoDefinida, self.acaoAnterior = self.defineAcao(
                        self.acao, self.acaoAnterior)  # Define a ação

                    # Zerando as váriaveis do escopo
                    self.acao = []

                    cv2.waitKey(15 * 33)

            # Codificação do frame para um .jpeg
            #ret, self.frame = cv2.imencode('.jpg', self.frame)
            # Converter o jpg em bytes e abaixo retorna o mesmo
            #self.frame = self.frame.tobytes()
            # yield (b'--frame\r\n'
            #       b'Content-Type: image/jpeg\r\n\r\n' + self.frame + b'\r\n\r\n')
            return "ok"

    def variaveis(self):
        acaoAgora = self.acaoDefinida
        self.acaoDefinida = 'nenhuma'

        # Evitar repetições de variáveis para melhor processamento dos comandos passados por piscadas
        return jsonify(acaoAgora)
