from threading import Thread
import pyttsx3

class Speech(Thread):
    # Método de reprodução da voz
    def playAudio(self,answer):
        self.engine = pyttsx3.init() # Inicializa a engine

        self.engine.setProperty('rate',125) # Pré define um rate

        self.engine.setProperty('volume',1.0) # Seta um volume padrão
        self.engine.say(answer)
        self.engine.runAndWait()

Speech().start()

Speech().playAudio("teste")