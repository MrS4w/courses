# GAME: Pedra Papel e Tesoura
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 12)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:      # Computador jogou PEDRA
    if jogador == 0:     # Jogador jogou PEDRA
        print('EMPATE!')
    elif jogador == 1:   # Jogador jogou PAPEL
        print('JOGADOR VENCE!')
    elif jogador == 2:   # Jogador jogou TESOURA
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:    # Computador jogou PAPEL
    if jogador == 0:     # Jogador jogou PEDRA
        print('COMPUTADOR VENCE!')
    elif jogador == 1:   # Jogador jogou PAPEL
        print('EMPATE!')
    elif jogador == 2:   # Jogador jogou TESOURA
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:    # Computador jogou TESOURA
    if jogador == 0:     # Jogador jogou PEDRA
        print('JOGADOR VENCE!')
    elif jogador == 1:   # Jogador jogou PAPEL
        print('COMPUTADOR VENCE!')
    elif jogador == 2:   # Jogador jogou TESOURA
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
