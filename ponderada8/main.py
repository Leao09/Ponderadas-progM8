import os
import sys
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound

def transcrever_traduzir_falar(caminho_audio):
    # Função para realizar a transcrição do áudio para texto
    def transcrever_audio(caminho_audio):
        reconhecedor = sr.Recognizer()
        arquivo_audio = sr.AudioFile(caminho_audio)
        
        with arquivo_audio as fonte:
            dados_audio = reconhecedor.record(fonte)
        
        try:
            texto = reconhecedor.recognize_google(dados_audio, language='pt-BR')
            return texto
        except sr.UnknownValueError:
            return "Não foi possível reconhecer a fala."
        except sr.RequestError:
            return "Erro na requisição ao serviço de reconhecimento de fala."

    # Função para traduzir o texto
    def traduzir_texto(texto):
        tradutor = Translator()
        traducao = tradutor.translate(texto, src='pt', dest='en')
        return traducao.text

    # Função para converter texto em fala e reproduzir
    def reproduzir_texto(texto):
        tts = gTTS(text=texto, lang='en')
        tts.save("videoplayback.mp3")
        playsound.playsound("videoplayback.mp3")
        os.remove("videoplayback.mp3")  # Remove o arquivo de áudio após reprodução

    texto_reconhecido = transcrever_audio(caminho_audio)
    if texto_reconhecido:
        print("Texto reconhecido:", texto_reconhecido)
        texto_traduzido = traduzir_texto(texto_reconhecido)
        print("Texto traduzido:", texto_traduzido)
        reproduzir_texto(texto_traduzido)
    else:
        print("Não foi possível reconhecer a fala no arquivo fornecido.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python nome_do_arquivo.py caminho_para_o_arquivo_de_audio")
    else:
        caminho_arquivo_audio = sys.argv[1]
        transcrever_traduzir_falar(caminho_arquivo_audio)