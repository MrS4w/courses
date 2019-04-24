# Maior e menor valores em Tupla
from random import randint

numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os valores sorteados são: ', end='')
for i in numeros:
    print(i, end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
