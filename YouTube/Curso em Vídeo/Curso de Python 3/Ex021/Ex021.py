# Tocando um MP3
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Tocando...\nDigite algo para cancelar: ')