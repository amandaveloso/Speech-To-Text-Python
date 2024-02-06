import speech_recognition as sr
import pandas as pd

# Caminho para o arquivo de áudio WAV
audio_path = 'audio.wav'

# Inicializar o reconhecedor
r = sr.Recognizer()

# Carregar o arquivo de áudio
with sr.AudioFile(audio_path) as source:
    audio_data = r.record(source)  # Ler o arquivo completo

# Tenta transcrever o áudio
try:
    text = r.recognize_google(audio_data, language='pt-BR')  # Substitua 'pt-BR' pelo idioma apropriado
    print("Transcrição do Áudio: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition não conseguiu entender o áudio")
except sr.RequestError as e:
    print(f"Erro ao solicitar resultados do serviço Google Speech Recognition; {e}")

text

import csv

# Abre um arquivo CSV para escrita
with open('audio_transcrito.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Escreve o texto em uma linha do arquivo CSV
    writer.writerow([text])
