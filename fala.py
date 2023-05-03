import gtts
from playsound import playsound

with open('texto.txt', 'r') as arquivo:
    for i in arquivo:
        frase = gtts.gTTS(i, lang='pt-br')#ou 'en-us'

        frase.save('frase.mp3')
        playsound('frase.mp3')
